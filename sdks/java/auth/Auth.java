// file: sdks/java/auth/Auth.java
// version: 1.0.0
// guid: 00cff2fe-2fc4-429f-bf34-f8185c7171c0

package sdks.java.auth;

/**
 * Authentication helpers.
 */
public class Auth {
  private String token;

  public Auth() {
    this.token = ""; // TODO: initialize token
  }

  public String getToken() {
    // TODO: return valid token
    return token;
  }

  public void refresh() {
    // TODO: refresh token
  }

  // TODO: add OAuth2 support
  // TODO: handle JWTs
  // TODO: support API keys
}
