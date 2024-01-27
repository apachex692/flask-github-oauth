# GitHub OAuth Flow Demonstration

This project demonstrates the OAuth2.0 flow for authorizing a Flask app to access a GitHub repository of a user.

- **Author:** Sakthi Santhosh
- **Created on:** 08/09/2023

## Introduction

OAuth, which stands for Open Authorization, is an industry-standard protocol for *authorization.* It enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner or by allowing the third-party application to obtain access on its own.

The primary goal of OAuth is to provide a secure and standardized way for users to *grant selective access to their resources without sharing their credentials.* This is particularly crucial in scenarios where users want to allow third-party applications to access their data on other websites, such as social media platforms, without compromising their login credentials.

OAuth operates through a series of interactions between three main parties: the resource owner (user), the client (third-party application), and the authorization server. These interactions result in the issuance of access tokens that the client can then use to access protected resources on behalf of the resource owner.

## Steps Involved

Certainly, Master Sakthi Santhosh. The OAuth flow involves several steps to enable secure authorization for accessing resources. Here's a detailed explanation:

1. **Client Registration:** The client (your application) registers with the authorization server. This involves obtaining a client ID and client secret, which are used to identify and authenticate the client.

2. **Authorization Request:** The client initiates the OAuth flow by redirecting the user to the authorization server with a request for authorization. This includes parameters like client ID, scope (permissions requested), and a redirect URI.

3. **User Authentication:** The authorization server authenticates the user. This step varies based on the grant type and can involve login, consent, or other authentication mechanisms.

4. **Authorization Grant:** If the user grants permission, the authorization server issues an authorization grant to the client. The grant type depends on the specific OAuth flow being used (e.g., authorization code, implicit, client credentials).

5. **Token Request:** The client uses the authorization grant to request an access token from the authorization server. This request includes the grant type, client credentials, and the authorization code (if applicable).

6. **Token Response:** The authorization server responds with an access token and optionally a refresh token. The access token is used to authenticate and authorize the client when accessing the protected resources.

7. **Resource Access:** The client can use the access token to make requests to the resource server (API). The token is usually included in the request header or as a parameter.

8. **Token Refresh (if applicable):** If a refresh token was issued, the client can use it to obtain a new access token without requiring user interaction. This helps in maintaining long-term access to resources.

9. **Access to Protected Resources:** The resource server verifies the access token and grants or denies access to the requested resources based on the token's validity and scope.

10. **Token Revocation (if applicable):** Optionally, there may be mechanisms for token revocation, allowing a user to invalidate previously granted access tokens.

This comprehensive flow ensures secure and authorized access to resources while maintaining user privacy and control over their data.

## Types of OAuth2.0 Flows

### 1. Authorization Code Flow

- **Used In:** Web Application with a Server Back-end (this project)
- **Steps Involved:**
    1. The web application makes a request to the authorization provider by redirecting the user.
    2. The user enters their credentials thereby providing a grant to the web application.
    3. The authorization provider then sends a code to the web application's back-end. The URL for sending this code is pre-defined by the web application developers in the authorization provider settings.
    4. The back-end, with the code received, makes a request to the authorization server (with client ID and client secret) to receive access/refresh tokens in exchange for the code. The code is invalidated (expires) after successful exchange for token. 
    5. With the access and refresh token in the back-end server, the back-end server can now access the protected resources of the user on behalf of them and send the information to the web application.

### 2. Implicit Code Flow

- **Used In:** Single Page Application (no back-end, completely runs off the browser)
- **Note:** Here, since the browser cannot save client secret securely, there is no exchange for tokens with code. Hence step-3 and step-4 of Authorization Code Flow (method-1) is not applicable here.
- **Steps Involved:**
    1. The SPA makes a request with the client ID to the authorization server.
    2. The user enters their credentials thereby providing a grant to the SPA.
    3. The authorization server after validating the user, sends tokens directly to the SPA.

### 3. Client Credentials Flow

- **Used In:** Server-Server Communication
- **Note:** Here, there is no user interaction. A server makes request to the authorization server with the client ID and secrets directly. This is useful when the server itself wants to authorize to a 3rd party service.
- **Steps Involved:**
    1. The backend service sends a request to the authorization server with its client ID and client secret.
    2. The authorization server verifies the client credentials and responds with an access token.
    3. The backend service can now use the obtained access token to make requests to the third-party API on its own behalf.

### 4. Resource Owner Password Credentials (ROPC) Flow

- **Used In:** Legacy or Highly Trusted Clients or Mobile Apps
- **Note:** Instead of the user entering the user credentials of the IdP in the IdP's website, the application itself takes it and sends it directly to the authorization (IdP) server thereby eliminating the redirection to the IdP website.
- **Steps Involved:**
    1. The user enters the credentials in the application.
    2. The application makes a request with the username and password to the authorization server (no client ID or client secret).
    3. The application, if the information sent is validated, receives the tokens.

## Contributing

This is a LAD project and I discourage submitting issues/public contributions. The repository has been kept public only for learning purpose.
