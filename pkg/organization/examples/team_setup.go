// file: pkg/organization/examples/team_setup.go
// version: 1.0.0
// guid: 3fa73561-d864-472e-aae8-bc2faf95a90f

package examples

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/organization/teams"
)

// ExampleTeamSetup demonstrates creating a team and managing membership.
func ExampleTeamSetup() {
	ctx := context.Background()
	tm := teams.NewManager()
	team := &teams.Team{ID: "t1", Name: "TeamOne"}
	_ = tm.CreateTeam(ctx, team)
	_ = tm.AddMember(ctx, "t1", "user1", teams.RoleOwner)
	_ = tm.AddMember(ctx, "t1", "user2", teams.RoleMember)
	members, _ := tm.Members(ctx, "t1")
	fmt.Printf("members: %d\n", len(members))
	// Output: members: 2
}
