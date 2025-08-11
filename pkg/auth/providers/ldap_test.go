// file: pkg/auth/providers/ldap_test.go
// version: 1.0.1
// guid: b2c3d4e5-f6a7-8091-b2c3-d4e5f6a7b8c9

//go:build integration

package providers

import (
	"context"
	"net"
	"testing"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/nmcclain/ldap"
)

func startLDAPServer(t *testing.T) (string, func()) {
	s := ldap.NewServer()
	userDN := "cn=alice,dc=example,dc=org"
	password := "password"
	s.BindFunc("", func(bindDN, bindPw string, conn net.Conn) (ldap.LDAPResultCode, error) {
		if bindDN == userDN && bindPw == password {
			return ldap.LDAPResultSuccess, nil
		}
		return ldap.LDAPResultInvalidCredentials, nil
	})
	s.SearchFunc("", func(boundDN string, req *ldap.SearchRequest, conn net.Conn) (ldap.ServerSearchResult, error) {
		entry := ldap.NewSearchResultEntry(userDN)
		entry.AddAttribute("dn", []string{userDN})
		return ldap.ServerSearchResult{Entries: []*ldap.Entry{entry}}, nil
	})
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatalf("listen: %v", err)
	}
	go s.Serve(ln)
	return "ldap://" + ln.Addr().String(), func() { s.Stop(); ln.Close() }
}

func TestLDAPProvider(t *testing.T) {
	addr, stop := startLDAPServer(t)
	defer stop()
	prov := NewLDAPProvider(addr, "dc=example,dc=org", "cn", []byte("secret"), nil)

	req := &proto.AuthenticateRequest{}
	creds := &proto.PasswordCredentials{}
	creds.SetUsername("alice")
	creds.SetPassword("password")
	req.SetPassword(creds)
	resp, err := prov.Authenticate(context.Background(), req)
	if err != nil {
		t.Fatalf("auth failed: %v", err)
	}
	vreq := &proto.ValidateTokenRequest{}
	vreq.SetAccessToken(resp.GetAccessToken())
	vresp, err := prov.ValidateToken(context.Background(), vreq)
	if err != nil || !vresp.GetValid() {
		t.Fatalf("validate failed")
	}
}
