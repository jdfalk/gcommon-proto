# Web Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 200
- **Messages**: 200

## Table of Contents

### Messages

- [`AddMiddlewareRequest`](#add_middleware_request) - from add_middleware_request.proto
- [`AddMiddlewareResponse`](#add_middleware_response) - from add_middleware_response.proto
- [`CORSConfig`](#cors_config) - from cors_config.proto
- [`CloseWebsocketRequest`](#close_websocket_request) - from close_websocket_request.proto
- [`CloseWebsocketResponse`](#close_websocket_response) - from close_websocket_response.proto
- [`ConfigureGlobalRequest`](#configure_global_request) - from configure_global_request.proto
- [`ConfigureGlobalResponse`](#configure_global_response) - from configure_global_response.proto
- [`CookieConfig`](#cookie_config) - from cookie_config.proto
- [`CookieData`](#cookie_data) - from cookie_data.proto
- [`CreateCookieRequest`](#create_cookie_request) - from create_cookie_request.proto
- [`CreateCookieResponse`](#create_cookie_response) - from create_cookie_response.proto
- [`CreateServerRequest`](#create_server_request) - from create_server_request.proto
- [`CreateServerResponse`](#create_server_response) - from create_server_response.proto
- [`CreateTemplateRequest`](#create_template_request) - from create_template_request.proto
- [`CreateTemplateResponse`](#create_template_response) - from create_template_response.proto
- [`CreateWebsocketRequest`](#create_websocket_request) - from create_websocket_request.proto
- [`CreateWebsocketResponse`](#create_websocket_response) - from create_websocket_response.proto
- [`CsrfConfig`](#csrf_config) - from csrf_config.proto
- [`DeleteCookieRequest`](#delete_cookie_request) - from delete_cookie_request.proto
- [`DeleteCookieResponse`](#delete_cookie_response) - from delete_cookie_response.proto
- [`DeleteFileRequest`](#delete_file_request) - from delete_file_request.proto
- [`DeleteFileResponse`](#delete_file_response) - from delete_file_response.proto
- [`DeleteTemplateRequest`](#delete_template_request) - from delete_template_request.proto
- [`DeleteTemplateResponse`](#delete_template_response) - from delete_template_response.proto
- [`DownloadFileRequest`](#download_file_request) - from download_file_request.proto
- [`DownloadFileResponse`](#download_file_response) - from download_file_response.proto
- [`ExportServerConfigRequest`](#export_server_config_request) - from export_server_config_request.proto
- [`ExportServerConfigResponse`](#export_server_config_response) - from export_server_config_response.proto
- [`FileInfo`](#file_info) - from file_info.proto
- [`FileMetadata`](#file_metadata) - from file_metadata.proto
- [`FileUpload`](#file_upload) - from file_upload.proto
- [`FlushCacheRequest`](#flush_cache_request) - from flush_cache_request.proto
- [`FlushCacheResponse`](#flush_cache_response) - from flush_cache_response.proto
- [`GenerateCsrfTokenRequest`](#generate_csrf_token_request) - from generate_csrf_token_request.proto
- [`GenerateCsrfTokenResponse`](#generate_csrf_token_response) - from generate_csrf_token_response.proto
- [`GetAccessLogsRequest`](#get_access_logs_request) - from get_access_logs_request.proto
- [`GetAccessLogsResponse`](#get_access_logs_response) - from get_access_logs_response.proto
- [`GetCacheConfigRequest`](#get_cache_config_request) - from get_cache_config_request.proto
- [`GetCacheConfigResponse`](#get_cache_config_response) - from get_cache_config_response.proto
- [`GetCookieRequest`](#get_cookie_request) - from get_cookie_request.proto
- [`GetCookieResponse`](#get_cookie_response) - from get_cookie_response.proto
- [`GetCorsConfigRequest`](#get_cors_config_request) - from get_cors_config_request.proto
- [`GetCorsConfigResponse`](#get_cors_config_response) - from get_cors_config_response.proto
- [`GetFileInfoRequest`](#get_file_info_request) - from get_file_info_request.proto
- [`GetFileInfoResponse`](#get_file_info_response) - from get_file_info_response.proto
- [`GetHandlerInfoRequest`](#get_handler_info_request) - from get_handler_info_request.proto
- [`GetHandlerInfoResponse`](#get_handler_info_response) - from get_handler_info_response.proto
- [`GetMiddlewareInfoRequest`](#get_middleware_info_request) - from get_middleware_info_request.proto
- [`GetMiddlewareInfoResponse`](#get_middleware_info_response) - from get_middleware_info_response.proto
- [`GetPerformanceStatsRequest`](#get_performance_stats_request) - from get_performance_stats_request.proto
- [`GetPerformanceStatsResponse`](#get_performance_stats_response) - from get_performance_stats_response.proto
- [`GetRouteInfoRequest`](#get_route_info_request) - from get_route_info_request.proto
- [`GetRouteInfoResponse`](#get_route_info_response) - from get_route_info_response.proto
- [`GetRouteMetricsRequest`](#get_route_metrics_request) - from get_route_metrics_request.proto
- [`GetRouteMetricsResponse`](#get_route_metrics_response) - from get_route_metrics_response.proto
- [`GetSSLCertificateInfoRequest`](#get_ssl_certificate_info_request) - from get_ssl_certificate_info_request.proto
- [`GetSSLCertificateInfoResponse`](#get_ssl_certificate_info_response) - from get_ssl_certificate_info_response.proto
- [`GetSecurityConfigRequest`](#get_security_config_request) - from get_security_config_request.proto
- [`GetSecurityConfigResponse`](#get_security_config_response) - from get_security_config_response.proto
- [`GetServerConfigRequest`](#get_server_config_request) - from get_server_config_request.proto
- [`GetServerConfigResponse`](#get_server_config_response) - from get_server_config_response.proto
- [`GetServerHealthRequest`](#get_server_health_request) - from get_server_health_request.proto
- [`GetServerHealthResponse`](#get_server_health_response) - from get_server_health_response.proto
- [`GetServerLogsRequest`](#get_server_logs_request) - from get_server_logs_request.proto
- [`GetServerLogsResponse`](#get_server_logs_response) - from get_server_logs_response.proto
- [`GetServerMetricsRequest`](#get_server_metrics_request) - from get_server_metrics_request.proto
- [`GetServerMetricsResponse`](#get_server_metrics_response) - from get_server_metrics_response.proto
- [`GetServerStatusRequest`](#get_server_status_request) - from get_server_status_request.proto
- [`GetServerStatusResponse`](#get_server_status_response) - from get_server_status_response.proto
- [`GetTemplateInfoRequest`](#get_template_info_request) - from get_template_info_request.proto
- [`GetTemplateInfoResponse`](#get_template_info_response) - from get_template_info_response.proto
- [`GetWebsocketInfoRequest`](#get_websocket_info_request) - from get_websocket_info_request.proto
- [`GetWebsocketInfoResponse`](#get_websocket_info_response) - from get_websocket_info_response.proto
- [`HandleRequest`](#handle_request) - from handle_request.proto
- [`HandleRequestRequest`](#handle_request_request) - from handle_request_request.proto
- [`HandleRequestResponse`](#handle_request_response) - from handle_request_response.proto
- [`HandleResponse`](#handle_response) - from handle_response.proto
- [`HandlerConfig`](#handler_config) - from handler_config.proto
- [`HandlerInfo`](#handler_info) - from handler_info.proto
- [`HttpHeader`](#http_header) - from http_header.proto
- [`HttpRequest`](#http_request) - from http_request.proto
- [`HttpResponse`](#http_response) - from http_response.proto
- [`ImportServerConfigRequest`](#import_server_config_request) - from import_server_config_request.proto
- [`ImportServerConfigResponse`](#import_server_config_response) - from import_server_config_response.proto
- [`ListCookiesRequest`](#list_cookies_request) - from list_cookies_request.proto
- [`ListCookiesResponse`](#list_cookies_response) - from list_cookies_response.proto
- [`ListFilesRequest`](#list_files_request) - from list_files_request.proto
- [`ListFilesResponse`](#list_files_response) - from list_files_response.proto
- [`ListHandlersRequest`](#list_handlers_request) - from list_handlers_request.proto
- [`ListHandlersResponse`](#list_handlers_response) - from list_handlers_response.proto
- [`ListMiddlewareRequest`](#list_middleware_request) - from list_middleware_request.proto
- [`ListMiddlewareResponse`](#list_middleware_response) - from list_middleware_response.proto
- [`ListRoutesRequest`](#list_routes_request) - from list_routes_request.proto
- [`ListRoutesResponse`](#list_routes_response) - from list_routes_response.proto
- [`ListServersRequest`](#list_servers_request) - from list_servers_request.proto
- [`ListServersResponse`](#list_servers_response) - from list_servers_response.proto
- [`ListTemplatesRequest`](#list_templates_request) - from list_templates_request.proto
- [`ListTemplatesResponse`](#list_templates_response) - from list_templates_response.proto
- [`ListWebsocketsRequest`](#list_websockets_request) - from list_websockets_request.proto
- [`ListWebsocketsResponse`](#list_websockets_response) - from list_websockets_response.proto
- [`MiddlewareConfig`](#middleware_config) - from middleware_config.proto
- [`MiddlewareInfo`](#middleware_info) - from middleware_info.proto
- [`MimeType`](#mime_type) - from mime_type.proto
- [`ProxyConfig`](#proxy_config) - from proxy_config.proto
- [`RegisterHandlerRequest`](#register_handler_request) - from register_handler_request.proto
- [`RegisterHandlerResponse`](#register_handler_response) - from register_handler_response.proto
- [`RegisterMiddlewareRequest`](#register_middleware_request) - from register_middleware_request.proto
- [`RegisterMiddlewareResponse`](#register_middleware_response) - from register_middleware_response.proto
- [`RegisterRouteRequest`](#register_route_request) - from register_route_request.proto
- [`RegisterRouteResponse`](#register_route_response) - from register_route_response.proto
- [`ReloadServerConfigRequest`](#reload_server_config_request) - from reload_server_config_request.proto
- [`ReloadServerConfigResponse`](#reload_server_config_response) - from reload_server_config_response.proto
- [`RemoveMiddlewareRequest`](#remove_middleware_request) - from remove_middleware_request.proto
- [`RemoveMiddlewareResponse`](#remove_middleware_response) - from remove_middleware_response.proto
- [`RenderTemplateRequest`](#render_template_request) - from render_template_request.proto
- [`RenderTemplateResponse`](#render_template_response) - from render_template_response.proto
- [`ResetStatsRequest`](#reset_stats_request) - from reset_stats_request.proto
- [`ResetStatsResponse`](#reset_stats_response) - from reset_stats_response.proto
- [`RestartServerRequest`](#restart_server_request) - from restart_server_request.proto
- [`RestartServerResponse`](#restart_server_response) - from restart_server_response.proto
- [`RouteConfig`](#route_config) - from route_config.proto
- [`RouteInfo`](#route_info) - from route_info.proto
- [`SendWebsocketMessageRequest`](#send_websocket_message_request) - from send_websocket_message_request.proto
- [`SendWebsocketMessageResponse`](#send_websocket_message_response) - from send_websocket_message_response.proto
- [`ServeStaticRequest`](#serve_static_request) - from serve_static_request.proto
- [`ServeStaticResponse`](#serve_static_response) - from serve_static_response.proto
- [`ServerConfig`](#server_config) - from server_config.proto
- [`ServerEvent`](#server_event) - from server_event.proto
- [`SessionData`](#session_data) - from session_data.proto
- [`SslConfig`](#ssl_config) - from ssl_config.proto
- [`StartServerRequest`](#start_server_request) - from start_server_request.proto
- [`StartServerResponse`](#start_server_response) - from start_server_response.proto
- [`StaticConfig`](#static_config) - from static_config.proto
- [`StopServerRequest`](#stop_server_request) - from stop_server_request.proto
- [`StopServerResponse`](#stop_server_response) - from stop_server_response.proto
- [`StreamServerEventsRequest`](#stream_server_events_request) - from stream_server_events_request.proto
- [`TemplateConfig`](#template_config) - from template_config.proto
- [`TemplateData`](#template_data) - from template_data.proto
- [`UnregisterHandlerRequest`](#unregister_handler_request) - from unregister_handler_request.proto
- [`UnregisterHandlerResponse`](#unregister_handler_response) - from unregister_handler_response.proto
- [`UnregisterMiddlewareRequest`](#unregister_middleware_request) - from unregister_middleware_request.proto
- [`UnregisterMiddlewareResponse`](#unregister_middleware_response) - from unregister_middleware_response.proto
- [`UnregisterRouteRequest`](#unregister_route_request) - from unregister_route_request.proto
- [`UnregisterRouteResponse`](#unregister_route_response) - from unregister_route_response.proto
- [`UpdateCacheConfigRequest`](#update_cache_config_request) - from update_cache_config_request.proto
- [`UpdateCacheConfigResponse`](#update_cache_config_response) - from update_cache_config_response.proto
- [`UpdateCookieRequest`](#update_cookie_request) - from update_cookie_request.proto
- [`UpdateCookieResponse`](#update_cookie_response) - from update_cookie_response.proto
- [`UpdateCorsConfigRequest`](#update_cors_config_request) - from update_cors_config_request.proto
- [`UpdateCorsConfigResponse`](#update_cors_config_response) - from update_cors_config_response.proto
- [`UpdateHandlerConfigRequest`](#update_handler_config_request) - from update_handler_config_request.proto
- [`UpdateHandlerConfigResponse`](#update_handler_config_response) - from update_handler_config_response.proto
- [`UpdateMiddlewareConfigRequest`](#update_middleware_config_request) - from update_middleware_config_request.proto
- [`UpdateMiddlewareConfigResponse`](#update_middleware_config_response) - from update_middleware_config_response.proto
- [`UpdateRouteConfigRequest`](#update_route_config_request) - from update_route_config_request.proto
- [`UpdateRouteConfigResponse`](#update_route_config_response) - from update_route_config_response.proto
- [`UpdateSSLCertificateRequest`](#update_ssl_certificate_request) - from update_ssl_certificate_request.proto
- [`UpdateSSLCertificateResponse`](#update_ssl_certificate_response) - from update_ssl_certificate_response.proto
- [`UpdateSecurityConfigRequest`](#update_security_config_request) - from update_security_config_request.proto
- [`UpdateSecurityConfigResponse`](#update_security_config_response) - from update_security_config_response.proto
- [`UpdateServerConfigRequest`](#update_server_config_request) - from update_server_config_request.proto
- [`UpdateServerConfigResponse`](#update_server_config_response) - from update_server_config_response.proto
- [`UploadFileRequest`](#upload_file_request) - from upload_file_request.proto
- [`UploadFileResponse`](#upload_file_response) - from upload_file_response.proto
- [`UrlPath`](#url_path) - from url_path.proto
- [`ValidateCsrfTokenRequest`](#validate_csrf_token_request) - from validate_csrf_token_request.proto
- [`ValidateCsrfTokenResponse`](#validate_csrf_token_response) - from validate_csrf_token_response.proto
- [`WebAuthConfig`](#auth_config) - from auth_config.proto
- [`WebAuthenticateRequest`](#authenticate_request) - from authenticate_request.proto
- [`WebAuthenticateResponse`](#authenticate_response) - from authenticate_response.proto
- [`WebAuthorizeRequest`](#authorize_request) - from authorize_request.proto
- [`WebAuthorizeResponse`](#authorize_response) - from authorize_response.proto
- [`WebCacheConfig`](#cache_config) - from cache_config.proto
- [`WebCompressionConfig`](#compression_config) - from compression_config.proto
- [`WebCreateSessionRequest`](#create_session_request) - from create_session_request.proto
- [`WebCreateSessionResponse`](#create_session_response) - from create_session_response.proto
- [`WebDeleteSessionRequest`](#delete_session_request) - from delete_session_request.proto
- [`WebDeleteSessionResponse`](#delete_session_response) - from delete_session_response.proto
- [`WebGetMetricsRequest`](#get_metrics_request) - from get_metrics_request.proto
- [`WebGetMetricsResponse`](#get_metrics_response) - from get_metrics_response.proto
- [`WebGetSessionRequest`](#get_session_request) - from get_session_request.proto
- [`WebGetSessionResponse`](#get_session_response) - from get_session_response.proto
- [`WebHealthCheckConfig`](#health_check_config) - from health_check_config.proto
- [`WebHealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`WebHealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`WebInfo`](#web) - from web.proto
- [`WebListSessionsRequest`](#list_sessions_request) - from list_sessions_request.proto
- [`WebListSessionsResponse`](#list_sessions_response) - from list_sessions_response.proto
- [`WebLoadBalancerConfig`](#load_balancer_config) - from load_balancer_config.proto
- [`WebPerformanceStats`](#performance_stats) - from performance_stats.proto
- [`WebRateLimitConfig`](#rate_limit_config) - from rate_limit_config.proto
- [`WebSecurityConfig`](#security_config) - from security_config.proto
- [`WebSessionConfig`](#session_config) - from session_config.proto
- [`WebTLSConfig`](#tls_config) - from tls_config.proto
- [`WebTimeoutConfig`](#timeout_config) - from timeout_config.proto
- [`WebUpdateSessionRequest`](#update_session_request) - from update_session_request.proto
- [`WebUpdateSessionResponse`](#update_session_response) - from update_session_response.proto
- [`WebsocketConfig`](#websocket_config) - from websocket_config.proto
- [`WebsocketInfo`](#websocket_info) - from websocket_info.proto
- [`WebsocketMessage`](#websocket_message) - from websocket_message.proto

### Files in this Module

- [auth_config.proto](#auth_config)
- [cache_config.proto](#cache_config)
- [compression_config.proto](#compression_config)
- [configure_global_request.proto](#configure_global_request)
- [configure_global_response.proto](#configure_global_response)
- [cookie_config.proto](#cookie_config)
- [cors_config.proto](#cors_config)
- [csrf_config.proto](#csrf_config)
- [export_server_config_request.proto](#export_server_config_request)
- [export_server_config_response.proto](#export_server_config_response)
- [get_cache_config_request.proto](#get_cache_config_request)
- [get_cache_config_response.proto](#get_cache_config_response)
- [get_cors_config_request.proto](#get_cors_config_request)
- [get_cors_config_response.proto](#get_cors_config_response)
- [get_security_config_request.proto](#get_security_config_request)
- [get_security_config_response.proto](#get_security_config_response)
- [get_server_config_request.proto](#get_server_config_request)
- [get_server_config_response.proto](#get_server_config_response)
- [handler_config.proto](#handler_config)
- [health_check_config.proto](#health_check_config)
- [import_server_config_request.proto](#import_server_config_request)
- [import_server_config_response.proto](#import_server_config_response)
- [load_balancer_config.proto](#load_balancer_config)
- [middleware_config.proto](#middleware_config)
- [proxy_config.proto](#proxy_config)
- [rate_limit_config.proto](#rate_limit_config)
- [reload_server_config_request.proto](#reload_server_config_request)
- [reload_server_config_response.proto](#reload_server_config_response)
- [route_config.proto](#route_config)
- [security_config.proto](#security_config)
- [server_config.proto](#server_config)
- [session_config.proto](#session_config)
- [ssl_config.proto](#ssl_config)
- [static_config.proto](#static_config)
- [template_config.proto](#template_config)
- [timeout_config.proto](#timeout_config)
- [tls_config.proto](#tls_config)
- [update_cache_config_request.proto](#update_cache_config_request)
- [update_cache_config_response.proto](#update_cache_config_response)
- [update_cors_config_request.proto](#update_cors_config_request)
- [update_cors_config_response.proto](#update_cors_config_response)
- [update_handler_config_request.proto](#update_handler_config_request)
- [update_handler_config_response.proto](#update_handler_config_response)
- [update_middleware_config_request.proto](#update_middleware_config_request)
- [update_middleware_config_response.proto](#update_middleware_config_response)
- [update_route_config_request.proto](#update_route_config_request)
- [update_route_config_response.proto](#update_route_config_response)
- [update_security_config_request.proto](#update_security_config_request)
- [update_security_config_response.proto](#update_security_config_response)
- [update_server_config_request.proto](#update_server_config_request)
- [update_server_config_response.proto](#update_server_config_response)
- [websocket_config.proto](#websocket_config)
- [cookie_data.proto](#cookie_data)
- [file_info.proto](#file_info)
- [file_metadata.proto](#file_metadata)
- [file_upload.proto](#file_upload)
- [handler_info.proto](#handler_info)
- [http_header.proto](#http_header)
- [middleware_info.proto](#middleware_info)
- [mime_type.proto](#mime_type)
- [performance_stats.proto](#performance_stats)
- [route_info.proto](#route_info)
- [session_data.proto](#session_data)
- [template_data.proto](#template_data)
- [url_path.proto](#url_path)
- [web.proto](#web)
- [websocket_info.proto](#websocket_info)
- [websocket_message.proto](#websocket_message)
- [add_middleware_request.proto](#add_middleware_request)
- [add_middleware_response.proto](#add_middleware_response)
- [authenticate_request.proto](#authenticate_request)
- [authenticate_response.proto](#authenticate_response)
- [authorize_request.proto](#authorize_request)
- [authorize_response.proto](#authorize_response)
- [close_websocket_request.proto](#close_websocket_request)
- [close_websocket_response.proto](#close_websocket_response)
- [create_cookie_request.proto](#create_cookie_request)
- [create_cookie_response.proto](#create_cookie_response)
- [create_server_request.proto](#create_server_request)
- [create_server_response.proto](#create_server_response)
- [create_session_request.proto](#create_session_request)
- [create_session_response.proto](#create_session_response)
- [create_template_request.proto](#create_template_request)
- [create_template_response.proto](#create_template_response)
- [create_websocket_request.proto](#create_websocket_request)
- [create_websocket_response.proto](#create_websocket_response)
- [delete_cookie_request.proto](#delete_cookie_request)
- [delete_cookie_response.proto](#delete_cookie_response)
- [delete_file_request.proto](#delete_file_request)
- [delete_file_response.proto](#delete_file_response)
- [delete_session_request.proto](#delete_session_request)
- [delete_session_response.proto](#delete_session_response)
- [delete_template_request.proto](#delete_template_request)
- [delete_template_response.proto](#delete_template_response)
- [download_file_request.proto](#download_file_request)
- [download_file_response.proto](#download_file_response)
- [flush_cache_request.proto](#flush_cache_request)
- [flush_cache_response.proto](#flush_cache_response)
- [generate_csrf_token_request.proto](#generate_csrf_token_request)
- [generate_csrf_token_response.proto](#generate_csrf_token_response)
- [get_access_logs_request.proto](#get_access_logs_request)
- [get_access_logs_response.proto](#get_access_logs_response)
- [get_cookie_request.proto](#get_cookie_request)
- [get_cookie_response.proto](#get_cookie_response)
- [get_file_info_request.proto](#get_file_info_request)
- [get_file_info_response.proto](#get_file_info_response)
- [get_handler_info_request.proto](#get_handler_info_request)
- [get_handler_info_response.proto](#get_handler_info_response)
- [get_metrics_request.proto](#get_metrics_request)
- [get_metrics_response.proto](#get_metrics_response)
- [get_middleware_info_request.proto](#get_middleware_info_request)
- [get_middleware_info_response.proto](#get_middleware_info_response)
- [get_performance_stats_request.proto](#get_performance_stats_request)
- [get_performance_stats_response.proto](#get_performance_stats_response)
- [get_route_info_request.proto](#get_route_info_request)
- [get_route_info_response.proto](#get_route_info_response)
- [get_route_metrics_request.proto](#get_route_metrics_request)
- [get_route_metrics_response.proto](#get_route_metrics_response)
- [get_server_health_request.proto](#get_server_health_request)
- [get_server_health_response.proto](#get_server_health_response)
- [get_server_logs_request.proto](#get_server_logs_request)
- [get_server_logs_response.proto](#get_server_logs_response)
- [get_server_metrics_request.proto](#get_server_metrics_request)
- [get_server_metrics_response.proto](#get_server_metrics_response)
- [get_server_status_request.proto](#get_server_status_request)
- [get_server_status_response.proto](#get_server_status_response)
- [get_session_request.proto](#get_session_request)
- [get_session_response.proto](#get_session_response)
- [get_ssl_certificate_info_request.proto](#get_ssl_certificate_info_request)
- [get_ssl_certificate_info_response.proto](#get_ssl_certificate_info_response)
- [get_template_info_request.proto](#get_template_info_request)
- [get_template_info_response.proto](#get_template_info_response)
- [get_websocket_info_request.proto](#get_websocket_info_request)
- [get_websocket_info_response.proto](#get_websocket_info_response)
- [handle_request.proto](#handle_request)
- [handle_request_request.proto](#handle_request_request)
- [handle_request_response.proto](#handle_request_response)
- [handle_response.proto](#handle_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [http_request.proto](#http_request)
- [http_response.proto](#http_response)
- [list_cookies_request.proto](#list_cookies_request)
- [list_cookies_response.proto](#list_cookies_response)
- [list_files_request.proto](#list_files_request)
- [list_files_response.proto](#list_files_response)
- [list_handlers_request.proto](#list_handlers_request)
- [list_handlers_response.proto](#list_handlers_response)
- [list_middleware_request.proto](#list_middleware_request)
- [list_middleware_response.proto](#list_middleware_response)
- [list_routes_request.proto](#list_routes_request)
- [list_routes_response.proto](#list_routes_response)
- [list_servers_request.proto](#list_servers_request)
- [list_servers_response.proto](#list_servers_response)
- [list_sessions_request.proto](#list_sessions_request)
- [list_sessions_response.proto](#list_sessions_response)
- [list_templates_request.proto](#list_templates_request)
- [list_templates_response.proto](#list_templates_response)
- [list_websockets_request.proto](#list_websockets_request)
- [list_websockets_response.proto](#list_websockets_response)
- [register_handler_request.proto](#register_handler_request)
- [register_handler_response.proto](#register_handler_response)
- [register_middleware_request.proto](#register_middleware_request)
- [register_middleware_response.proto](#register_middleware_response)
- [register_route_request.proto](#register_route_request)
- [register_route_response.proto](#register_route_response)
- [remove_middleware_request.proto](#remove_middleware_request)
- [remove_middleware_response.proto](#remove_middleware_response)
- [render_template_request.proto](#render_template_request)
- [render_template_response.proto](#render_template_response)
- [reset_stats_request.proto](#reset_stats_request)
- [reset_stats_response.proto](#reset_stats_response)
- [restart_server_request.proto](#restart_server_request)
- [restart_server_response.proto](#restart_server_response)
- [send_websocket_message_request.proto](#send_websocket_message_request)
- [send_websocket_message_response.proto](#send_websocket_message_response)
- [serve_static_request.proto](#serve_static_request)
- [serve_static_response.proto](#serve_static_response)
- [start_server_request.proto](#start_server_request)
- [start_server_response.proto](#start_server_response)
- [stop_server_request.proto](#stop_server_request)
- [stop_server_response.proto](#stop_server_response)
- [unregister_handler_request.proto](#unregister_handler_request)
- [unregister_handler_response.proto](#unregister_handler_response)
- [unregister_middleware_request.proto](#unregister_middleware_request)
- [unregister_middleware_response.proto](#unregister_middleware_response)
- [unregister_route_request.proto](#unregister_route_request)
- [unregister_route_response.proto](#unregister_route_response)
- [update_cookie_request.proto](#update_cookie_request)
- [update_cookie_response.proto](#update_cookie_response)
- [update_session_request.proto](#update_session_request)
- [update_session_response.proto](#update_session_response)
- [update_ssl_certificate_request.proto](#update_ssl_certificate_request)
- [update_ssl_certificate_response.proto](#update_ssl_certificate_response)
- [upload_file_request.proto](#upload_file_request)
- [upload_file_response.proto](#upload_file_response)
- [validate_csrf_token_request.proto](#validate_csrf_token_request)
- [validate_csrf_token_response.proto](#validate_csrf_token_response)
- [server_event.proto](#server_event)
- [stream_server_events_request.proto](#stream_server_events_request)

---


## Messages Documentation

### auth_config.proto {#auth_config}

**Path**: `gcommon/v1/web/auth_config.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebAuthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/auth_config.proto
// version: 1.0.0
// guid: 01c8f7e0-20a4-4ffe-81ba-5e0aede462e0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthConfig message definition.
// AuthConfig defines authentication settings for a web server.
message WebAuthConfig {
  // Enable authentication middleware
  bool enable_auth = 1;

  // Allowed roles for access control
  repeated string allowed_roles = 2 [(buf.validate.field).repeated.min_items = 1];

  // Required scopes for authorization
  repeated string required_scopes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Additional auth options
  map<string, string> options = 4;
}
```

---

### cache_config.proto {#cache_config}

**Path**: `gcommon/v1/web/cache_config.proto` **Package**: `gcommon.v1.web` **Lines**: 37

**Messages** (1): `WebCacheConfig`

**Imports** (5):

- `gcommon/v1/common/cache_policy.proto`
- `gcommon/v1/common/cache_strategy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cache_config.proto
// version: 1.1.0
// guid: 21e9abdf-bf09-4c22-b45b-eb9c092d9664

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cache_policy.proto";
import "gcommon/v1/common/cache_strategy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CacheConfig defines caching behavior for web responses.
message WebCacheConfig {
  // Selected cache strategy for responses
  gcommon.v1.common.CacheStrategy strategy = 1;

  // Detailed cache policy settings
  gcommon.v1.common.CachePolicy policy = 2 [lazy = true];

  // Override time to live for web resources
  google.protobuf.Duration ttl = 3;

  // Whether caching is enabled for this server
  bool enabled = 4;

  // Optional namespace or cache name
  string cache_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### compression_config.proto {#compression_config}

**Path**: `gcommon/v1/web/compression_config.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Messages** (1): `WebCompressionConfig`

**Imports** (3):

- `gcommon/v1/common/compression_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/compression_config.proto
// version: 1.1.0
// guid: e4d9d1fd-7180-432c-a64b-5b6f24858928

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/compression_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CompressionConfig message definition.
message WebCompressionConfig {
  // Compression algorithm to use for HTTP responses
  // Compression type to use for responses
  gcommon.v1.common.LogCompressionType compression_type = 1;

  // Minimum content length in bytes before compression is applied
  int32 min_length = 2 [(buf.validate.field).int32.gte = 0];

  // Compression level (implementation specific)
  int32 level = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### configure_global_request.proto {#configure_global_request}

**Path**: `gcommon/v1/web/configure_global_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ConfigureGlobalRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/configure_global_request.proto
// version: 1.0.1
// guid: 53f1a181-4823-4590-977d-dcd614b74421

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ConfigureGlobalRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ConfigureGlobalRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### configure_global_response.proto {#configure_global_response}

**Path**: `gcommon/v1/web/configure_global_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ConfigureGlobalResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/configure_global_response.proto
// version: 1.0.1
// guid: 0719dc91-a213-44de-817e-6f26efe9dc68

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ConfigureGlobalResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ConfigureGlobalResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### cookie_config.proto {#cookie_config}

**Path**: `gcommon/v1/web/cookie_config.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `CookieConfig`

**Imports** (4):

- `gcommon/v1/common/cookie_same_site.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cookie_config.proto
// version: 1.1.0
// guid: 57c9187b-fa13-46bb-9840-d7a2515e7ff1

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cookie_same_site.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CookieConfig message definition.
message CookieConfig {
  // Cookie name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cookie domain
  string domain = 2;

  // Cookie path
  string path = 3;

  // Set Secure flag
  bool secure = 4;

  // Set HttpOnly flag
  bool http_only = 5;

  // SameSite policy
  gcommon.v1.common.CookieSameSite same_site = 6;

  // Max age of the cookie
  google.protobuf.Duration max_age = 7;
}
```

---

### cors_config.proto {#cors_config}

**Path**: `gcommon/v1/web/cors_config.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `CORSConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cors_config.proto
// version: 1.0.1
// guid: a30ac136-585a-4ceb-becf-9ca8beef5e86

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CorsConfig message definition.
message CORSConfig {
  // Enable CORS
  bool enabled = 1;

  // Allowed origins
  repeated string allowed_origins = 2 [(buf.validate.field).repeated.min_items = 1];

  // Allowed methods
  repeated string allowed_methods = 3 [(buf.validate.field).repeated.min_items = 1];

  // Allowed headers
  repeated string allowed_headers = 4 [(buf.validate.field).repeated.min_items = 1];

  // Exposed headers
  repeated string exposed_headers = 5 [(buf.validate.field).repeated.min_items = 1];

  // Allow credentials
  bool allow_credentials = 6;

  // Max age
  google.protobuf.Duration max_age = 7;
}
```

---

### csrf_config.proto {#csrf_config}

**Path**: `gcommon/v1/web/csrf_config.proto` **Package**: `gcommon.v1.web` **Lines**: 38

**Messages** (1): `CsrfConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/csrf_config.proto
// version: 1.1.0
// guid: b3eaed64-1234-45b9-86c4-e348b91cdbe9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CsrfConfig message definition.
message CsrfConfig {
  // Name of the HTTP header containing the CSRF token
  string header_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Name of the cookie used to store the token
  string cookie_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Length of generated tokens
  int32 token_length = 3;

  // Token expiration duration
  google.protobuf.Duration token_ttl = 4;

  // Require secure cookies
  bool secure = 5;
}
```

---

### export_server_config_request.proto {#export_server_config_request}

**Path**: `gcommon/v1/web/export_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ExportServerConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/export_server_config_request.proto
// version: 1.0.1
// guid: f5105c4f-0736-4a4a-a9c6-004a43fbbd9b

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ExportServerConfigRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ExportServerConfigRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### export_server_config_response.proto {#export_server_config_response}

**Path**: `gcommon/v1/web/export_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ExportServerConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/export_server_config_response.proto
// version: 1.0.1
// guid: b7274c09-ff07-4507-8c91-b7bfc995a64b

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ExportServerConfigResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ExportServerConfigResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_cache_config_request.proto {#get_cache_config_request}

**Path**: `gcommon/v1/web/get_cache_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetCacheConfigRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cache_config_request.proto
// version: 1.0.1
// guid: abc12345-6789-0def-1234-567890abcdef

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message GetCacheConfigRequest {
  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 1;
}
```

---

### get_cache_config_response.proto {#get_cache_config_response}

**Path**: `gcommon/v1/web/get_cache_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `GetCacheConfigResponse`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/cache_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cache_config_response.proto
// version: 1.0.1
// guid: def67890-abcd-1234-5678-90abcdef1234

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/cache_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message GetCacheConfigResponse {
  // The current cache configuration
  WebCacheConfig config = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_cors_config_request.proto {#get_cors_config_request}

**Path**: `gcommon/v1/web/get_cors_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCorsConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cors_config_request.proto
// version: 1.0.0
// guid: c22a2431-29be-4eb5-8ed8-40b2840f03ae

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCorsConfigRequest request definition.
message GetCorsConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_cors_config_response.proto {#get_cors_config_response}

**Path**: `gcommon/v1/web/get_cors_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCorsConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cors_config_response.proto
// version: 1.0.0
// guid: 15367ee2-9586-4b6b-a32f-69bf3a2f3310

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCorsConfigResponse response definition.
message GetCorsConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_security_config_request.proto {#get_security_config_request}

**Path**: `gcommon/v1/web/get_security_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetSecurityConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_security_config_request.proto
// version: 1.0.0
// guid: a5853c6e-88c2-4c4c-962b-c7fc36d4bdef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSecurityConfigRequest request definition.
message GetSecurityConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_security_config_response.proto {#get_security_config_response}

**Path**: `gcommon/v1/web/get_security_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetSecurityConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_security_config_response.proto
// version: 1.0.0
// guid: ad8fcfc2-e9a0-4a3c-8f15-eddc7235c96f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSecurityConfigResponse response definition.
message GetSecurityConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_server_config_request.proto {#get_server_config_request}

**Path**: `gcommon/v1/web/get_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_config_request.proto
// version: 1.0.0
// guid: 78c28db0-b087-4225-b72d-babf47e86db3

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerConfigRequest request definition.
message GetServerConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_server_config_response.proto {#get_server_config_response}

**Path**: `gcommon/v1/web/get_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_config_response.proto
// version: 1.0.0
// guid: 3f909fa5-4f36-4285-8b01-fe1bc5b01fd7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerConfigResponse response definition.
message GetServerConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### handler_config.proto {#handler_config}

**Path**: `gcommon/v1/web/handler_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `HandlerConfig`

**Imports** (4):

- `gcommon/v1/common/handler_type.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handler_config.proto
// version: 1.1.0
// guid: 68d30216-8b75-4c02-88ca-9c39d70d4c4c

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/handler_type.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandlerConfig message definition.
message HandlerConfig {
  // Handler type
  gcommon.v1.common.HandlerType type = 1;

  // Handler-specific configuration
  google.protobuf.Any config = 2;

  // Target for the handler (URL, function name, etc.)
  string target = 3 [(buf.validate.field).string.min_len = 1];

  // Additional handler options
  map<string, string> options = 4;
}
```

---

### health_check_config.proto {#health_check_config}

**Path**: `gcommon/v1/web/health_check_config.proto` **Package**: `gcommon.v1.web` **Lines**: 35

**Messages** (1): `WebHealthCheckConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/health_check_config.proto
// version: 1.1.0
// guid: 7aea6b7c-133f-4443-b7b6-c1cdeb194f0b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HealthCheckConfig defines parameters for performing HTTP health checks.
message WebHealthCheckConfig {
  // HTTP path used for the health check request.
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // Interval between health checks in seconds.
  double interval_seconds = 2 [(buf.validate.field).double.gte = 0.0];

  // Timeout for a single health check in seconds.
  double timeout_seconds = 3 [(buf.validate.field).double.gte = 0.0];

  // Expected HTTP status code indicating a healthy response.
  int32 expected_status = 4 [(buf.validate.field).int32.gte = 0];

  // Additional headers to include with the request.
  map<string, string> headers = 5;

  // Whether the health check is enabled.
  bool enabled = 6;
}
```

---

### import_server_config_request.proto {#import_server_config_request}

**Path**: `gcommon/v1/web/import_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ImportServerConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/import_server_config_request.proto
// version: 1.0.1
// guid: 60a97ec8-a4f9-4606-844c-774a208ca62a

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ImportServerConfigRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ImportServerConfigRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### import_server_config_response.proto {#import_server_config_response}

**Path**: `gcommon/v1/web/import_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ImportServerConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/import_server_config_response.proto
// version: 1.0.1
// guid: 5cf8e464-8b8e-487d-86a0-0707a9490356

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ImportServerConfigResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ImportServerConfigResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### load_balancer_config.proto {#load_balancer_config}

**Path**: `gcommon/v1/web/load_balancer_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `WebLoadBalancerConfig`

**Imports** (4):

- `gcommon/v1/common/load_balance_strategy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/load_balancer_config.proto
// version: 1.1.0
// guid: 773a3c4c-d370-4416-b0d8-bf270ea7d2de

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/load_balance_strategy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// LoadBalancerConfig message definition.
message WebLoadBalancerConfig {
  // Load balancing strategy
  gcommon.v1.common.LoadBalanceStrategy strategy = 1;

  // Upstream server addresses
  repeated string upstreams = 2 [(buf.validate.field).repeated.min_items = 1];

  // Health check path
  string health_check_path = 3 [(buf.validate.field).string.min_len = 1];

  // Timeout for proxy requests
  google.protobuf.Duration timeout = 4;
}
```

---

### middleware_config.proto {#middleware_config}

**Path**: `gcommon/v1/web/middleware_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `MiddlewareConfig`

**Imports** (3):

- `gcommon/v1/common/middleware_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/middleware_config.proto
// version: 1.0.0
// guid: e9b024e1-e72c-48e4-b1c4-5df34ed3e3ac

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/middleware_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// MiddlewareConfig message definition.
// MiddlewareConfig represents a single middleware's configuration.
message MiddlewareConfig {
  // Middleware type
  gcommon.v1.common.MiddlewareType type = 1;

  // Whether the middleware is enabled
  bool enabled = 2;

  // Execution priority (lower runs first)
  int32 priority = 3 [(buf.validate.field).int32.gte = 0];

  // Additional middleware options
  map<string, string> options = 4;
}
```

---

### proxy_config.proto {#proxy_config}

**Path**: `gcommon/v1/web/proxy_config.proto` **Package**: `gcommon.v1.web` **Lines**: 34

**Messages** (1): `ProxyConfig`

**Imports** (5):

- `gcommon/v1/common/proxy_type.proto`
- `gcommon/v1/web/http_header.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/proxy_config.proto
// version: 1.1.0
// guid: 44849c54-6bf7-4211-a8c0-0be1e0c98add

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/proxy_type.proto";
import "gcommon/v1/web/http_header.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ProxyConfig message definition.
message ProxyConfig {
  // Type of proxy
  gcommon.v1.common.ProxyType proxy_type = 1;

  // Target backend URL
  string target_url = 2 [ (buf.validate.field).string.uri = true ];

  // Headers to forward to the backend
  repeated HttpHeader forward_headers = 3;

  // Connect timeout duration
  google.protobuf.Duration connect_timeout = 4;

  // Whether to trust X-Forwarded headers
  bool trust_forward_headers = 5;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/web/rate_limit_config.proto` **Package**: `gcommon.v1.web` **Lines**: 36

**Messages** (1): `WebRateLimitConfig`

**Imports** (3):

- `gcommon/v1/common/rate_limit_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/rate_limit_config.proto
// version: 1.0.1
// guid: 180cb5f4-1064-4b88-bbe6-dbc6934ec21e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/rate_limit_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RateLimitConfig message definition.
message WebRateLimitConfig {
  // Enable rate limiting
  bool enabled = 1;

  // Requests per second
  int32 requests_per_second = 2 [(buf.validate.field).int32.gte = 0];

  // Burst size
  int32 burst_size = 3 [(buf.validate.field).int32.gte = 0];

  // Rate limit strategy
  gcommon.v1.common.RateLimitStrategy strategy = 4;

  // Rate limit key extractor
  string key_extractor = 5 [(buf.validate.field).string.min_len = 1];

  // Skip conditions
  repeated string skip_conditions = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### reload_server_config_request.proto {#reload_server_config_request}

**Path**: `gcommon/v1/web/reload_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ReloadServerConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reload_server_config_request.proto
// version: 1.0.1
// guid: abeb1b6f-6a94-4044-b27e-a91c1c9e6042

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ReloadServerConfigRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ReloadServerConfigRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### reload_server_config_response.proto {#reload_server_config_response}

**Path**: `gcommon/v1/web/reload_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ReloadServerConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reload_server_config_response.proto
// version: 1.0.1
// guid: a6f6a4cf-253b-4759-a0a7-f699c4cf8463

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ReloadServerConfigResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ReloadServerConfigResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### route_config.proto {#route_config}

**Path**: `gcommon/v1/web/route_config.proto` **Package**: `gcommon.v1.web` **Lines**: 37

**Messages** (1): `RouteConfig`

**Imports** (4):

- `gcommon/v1/common/handler_type.proto`
- `gcommon/v1/common/http_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/route_config.proto
// version: 1.1.0
// guid: ce3f0233-7da2-4e81-8460-b1bf3a6fba53

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/handler_type.proto";
import "gcommon/v1/common/http_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RouteConfig message definition.
message RouteConfig {
  // URL path pattern
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // Allowed HTTP methods
  repeated gcommon.v1.common.HTTPMethod methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Handler name or identifier
  string handler = 3 [(buf.validate.field).string.min_len = 1];

  // Handler type implementation
  gcommon.v1.common.HandlerType handler_type = 4;

  // Middleware IDs applied to this route
  repeated string middleware_ids = 5 [(buf.validate.field).repeated.min_items = 1];

  // Require authentication for route
  bool auth_required = 6;
}
```

---

### security_config.proto {#security_config}

**Path**: `gcommon/v1/web/security_config.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebSecurityConfig`

**Imports** (3):

- `gcommon/v1/web/tls_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/security_config.proto
// version: 1.1.0
// guid: 2d5231ca-5b58-4b11-8448-a87d4ae0154e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/tls_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SecurityConfig message definition.
message WebSecurityConfig {
  // Enable TLS security
  bool enable_tls = 1;

  // TLS configuration details
  WebTLSConfig tls = 2;

  // Allowed host patterns
  repeated string allowed_hosts = 3 [(buf.validate.field).repeated.min_items = 1];

  // Additional security options
  map<string, string> options = 4;
}
```

---

### server_config.proto {#server_config}

**Path**: `gcommon/v1/web/server_config.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `ServerConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_config.proto
// version: 1.0.0
// guid: f4e56c59-17af-4da2-8a92-e1a619fe9fba

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ServerConfig message definition.
// ServerConfig defines basic web server settings.
message ServerConfig {
  // Hostname or IP address to bind
  string host = 1 [(buf.validate.field).string.min_len = 1];

  // Listening port number
  int32 port = 2 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Enable TLS for secure communication
  bool enable_tls = 3;

  // Path to TLS certificate
  string tls_cert_path = 4 [(buf.validate.field).string.min_len = 1];

  // Path to TLS key
  string tls_key_path = 5 [(buf.validate.field).string.min_len = 1];

  // Trusted proxy addresses
  repeated string trusted_proxies = 6 [(buf.validate.field).repeated.min_items = 1];

  // Additional server options
  map<string, string> options = 7;
}
```

---

### session_config.proto {#session_config}

**Path**: `gcommon/v1/web/session_config.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `WebSessionConfig`

**Imports** (4):

- `gcommon/v1/common/cookie_same_site.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/session_config.proto
// version: 1.1.0
// guid: 78ffbac0-1dba-4e18-85e1-ecce179da015

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cookie_same_site.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SessionConfig message definition.
message WebSessionConfig {
  // Session idle timeout before automatic expiration
  google.protobuf.Duration idle_timeout = 1;

  // Absolute session lifetime regardless of activity
  google.protobuf.Duration absolute_timeout = 2;

  // Name of the session cookie
  string cookie_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Use secure cookies (HTTPS only)
  bool secure_cookies = 4;

  // Restrict cookie to HTTP only
  bool http_only = 5;

  // Cookie SameSite policy
  gcommon.v1.common.CookieSameSite same_site = 6;
}
```

---

### ssl_config.proto {#ssl_config}

**Path**: `gcommon/v1/web/ssl_config.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Messages** (1): `SslConfig`

**Imports** (3):

- `gcommon/v1/common/ssl_protocol.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/ssl_config.proto
// version: 1.1.0
// guid: 4d5ec783-ec4b-4ffc-a7e6-28df5382a594

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/ssl_protocol.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SslConfig message definition.
message SslConfig {
  // TLS protocol version
  gcommon.v1.common.SSLProtocol protocol = 1;

  // Path to certificate file
  string cert_file = 2 [(buf.validate.field).string.min_len = 1];

  // Path to key file
  string key_file = 3 [(buf.validate.field).string.min_len = 1];

  // Optional CA bundle path
  string ca_file = 4 [(buf.validate.field).string.min_len = 1];

  // Require client certificates
  bool require_client_auth = 5;
}
```

---

### static_config.proto {#static_config}

**Path**: `gcommon/v1/web/static_config.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `StaticConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/static_config.proto
// version: 1.1.0
// guid: e2d0d32a-6b50-42ec-b728-ef60869cf5ac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StaticConfig message definition.
message StaticConfig {
  // Root directory for static files
  string directory = 1 [(buf.validate.field).string.min_len = 1];

  // Default index files
  repeated string index_files = 2 [(buf.validate.field).repeated.min_items = 1];

  // Enable directory listing
  bool enable_listing = 3;
}
```

---

### template_config.proto {#template_config}

**Path**: `gcommon/v1/web/template_config.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `TemplateConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/template_config.proto
// version: 1.1.0
// guid: 02942f54-029c-468f-85df-cdf3042e8ee6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// TemplateConfig message definition.
message TemplateConfig {
  // Directory containing template files
  string directory = 1 [(buf.validate.field).string.min_len = 1];

  // Default file extension
  string extension = 2 [(buf.validate.field).string.min_len = 1];

  // Reload templates on change
  bool reload = 3;

  // Custom template function names
  repeated string functions = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### timeout_config.proto {#timeout_config}

**Path**: `gcommon/v1/web/timeout_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `WebTimeoutConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/timeout_config.proto
// version: 1.0.1
// guid: e3a21e33-e66f-47e7-b7ff-6c6df8a0e9a1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// TimeoutConfig specifies various timeout settings for the server.
message WebTimeoutConfig {
  // Read timeout
  google.protobuf.Duration read_timeout = 1;

  // Write timeout
  google.protobuf.Duration write_timeout = 2;

  // Idle timeout
  google.protobuf.Duration idle_timeout = 3;

  // Request timeout
  google.protobuf.Duration request_timeout = 4;

  // Shutdown timeout
  google.protobuf.Duration shutdown_timeout = 5;
}
```

---

### tls_config.proto {#tls_config}

**Path**: `gcommon/v1/web/tls_config.proto` **Package**: `gcommon.v1.web` **Lines**: 71

**Messages** (1): `WebTLSConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/tls_config.proto
// version: 1.0.0
// guid: 9f8e7d6c-5b4a-3928-1706-f5e4d3c2b1a0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
// Standard imports
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * TLSConfig defines TLS/SSL configuration for web servers.
 */
message WebTLSConfig {
  // Required fields (1-10)

  /**
   * Certificate file path or content.
   */
  string cert_file = 1;

  /**
   * Private key file path or content.
   */
  string key_file = 2;

  // Optional fields (11-50)

  /**
   * CA certificate file path for client verification.
   */
  string ca_file = 11;

  /**
   * Minimum TLS version (e.g., "1.2", "1.3").
   */
  string min_version = 12;

  /**
   * Maximum TLS version (e.g., "1.2", "1.3").
   */
  string max_version = 13;

  /**
   * List of supported cipher suites.
   */
  repeated string cipher_suites = 14;

  /**
   * Whether to require client certificates.
   */
  bool require_client_cert = 15;

  /**
   * Whether to verify client certificates.
   */
  bool verify_client_cert = 16;

  /**
   * Server name for SNI (Server Name Indication).
   */
  string server_name = 17 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### update_cache_config_request.proto {#update_cache_config_request}

**Path**: `gcommon/v1/web/update_cache_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `UpdateCacheConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/cache_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cache_config_request.proto
// version: 1.0.1
// guid: ghi12345-6789-0abc-def1-234567890123

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/cache_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UpdateCacheConfigRequest {
  // The new cache configuration to apply
  WebCacheConfig config = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### update_cache_config_response.proto {#update_cache_config_response}

**Path**: `gcommon/v1/web/update_cache_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Messages** (1): `UpdateCacheConfigResponse`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cache_config_response.proto
// version: 1.0.1
// guid: jkl45678-90ab-cdef-1234-567890abcdef

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UpdateCacheConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### update_cors_config_request.proto {#update_cors_config_request}

**Path**: `gcommon/v1/web/update_cors_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCorsConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cors_config_request.proto
// version: 1.0.0
// guid: 00b7b190-69c5-49c8-8b50-ca9c0e68e231

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCorsConfigRequest request definition.
message UpdateCorsConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_cors_config_response.proto {#update_cors_config_response}

**Path**: `gcommon/v1/web/update_cors_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCorsConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cors_config_response.proto
// version: 1.0.0
// guid: 44e8600c-ebb5-45be-851d-41f41c810996

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCorsConfigResponse response definition.
message UpdateCorsConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_handler_config_request.proto {#update_handler_config_request}

**Path**: `gcommon/v1/web/update_handler_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateHandlerConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_handler_config_request.proto
// version: 1.0.0
// guid: 6241c28b-b274-4d3e-afb4-2c2a65fa5e96

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateHandlerConfigRequest request definition.
message UpdateHandlerConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_handler_config_response.proto {#update_handler_config_response}

**Path**: `gcommon/v1/web/update_handler_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateHandlerConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_handler_config_response.proto
// version: 1.0.0
// guid: f5dc02ec-1a36-4fcd-ae1e-352189358ea7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateHandlerConfigResponse response definition.
message UpdateHandlerConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_middleware_config_request.proto {#update_middleware_config_request}

**Path**: `gcommon/v1/web/update_middleware_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Messages** (1): `UpdateMiddlewareConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/middleware_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_middleware_config_request.proto
// version: 1.0.1
// guid: 30e082c9-2bd6-4472-ae4a-f71e481f04a3
// UpdateMiddlewareConfigRequest request definition.
// UpdateMiddlewareConfigRequest updates an existing middleware configuration.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/middleware_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UpdateMiddlewareConfigRequest {
  // Request metadata for tracing and auth
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Updated middleware configuration
  MiddlewareConfig config = 2;
}
```

---

### update_middleware_config_response.proto {#update_middleware_config_response}

**Path**: `gcommon/v1/web/update_middleware_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `UpdateMiddlewareConfigResponse`

**Imports** (2):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_middleware_config_response.proto
// version: 1.0.1
// guid: e8328b61-1bdf-487b-b874-01de9424625e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateMiddlewareConfigResponse response definition.
// UpdateMiddlewareConfigResponse returns the result of updating middleware config.
message UpdateMiddlewareConfigResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Whether the middleware was updated
  bool updated = 2;
}
```

---

### update_route_config_request.proto {#update_route_config_request}

**Path**: `gcommon/v1/web/update_route_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateRouteConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_route_config_request.proto
// version: 1.0.0
// guid: 65c64e7e-be8d-4fa3-9bd1-e0c9b752fef9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateRouteConfigRequest request definition.
message UpdateRouteConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_route_config_response.proto {#update_route_config_response}

**Path**: `gcommon/v1/web/update_route_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateRouteConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_route_config_response.proto
// version: 1.0.0
// guid: 07ee551d-a9ae-4d39-995c-3442717c934b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateRouteConfigResponse response definition.
message UpdateRouteConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_security_config_request.proto {#update_security_config_request}

**Path**: `gcommon/v1/web/update_security_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateSecurityConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_security_config_request.proto
// version: 1.0.0
// guid: 69e8edc6-5475-4f71-9753-26c412daab0e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSecurityConfigRequest request definition.
message UpdateSecurityConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_security_config_response.proto {#update_security_config_response}

**Path**: `gcommon/v1/web/update_security_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateSecurityConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_security_config_response.proto
// version: 1.0.0
// guid: 63689787-044d-4302-8175-9745ac688e61

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSecurityConfigResponse response definition.
message UpdateSecurityConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_server_config_request.proto {#update_server_config_request}

**Path**: `gcommon/v1/web/update_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateServerConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_server_config_request.proto
// version: 1.0.0
// guid: 6a2b47b4-af5e-4e51-9807-18898846cb4a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateServerConfigRequest request definition.
message UpdateServerConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_server_config_response.proto {#update_server_config_response}

**Path**: `gcommon/v1/web/update_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateServerConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_server_config_response.proto
// version: 1.0.0
// guid: db0184f3-c771-45f7-946e-aaadcf2ba967

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateServerConfigResponse response definition.
message UpdateServerConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### websocket_config.proto {#websocket_config}

**Path**: `gcommon/v1/web/websocket_config.proto` **Package**: `gcommon.v1.web` **Lines**: 32

**Messages** (1): `WebsocketConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/websocket_config.proto
// version: 1.1.0
// guid: b746de14-1e1e-4faf-812f-0bf9fa38c201

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// WebsocketConfig message definition.
message WebsocketConfig {
  // Endpoint path for websocket connections
  string endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Allowed origin hosts
  repeated string allowed_origins = 2 [(buf.validate.field).repeated.min_items = 1];

  // Enable per-message compression
  bool enable_compression = 3;

  // Read buffer size in bytes
  int32 read_buffer_size = 4 [(buf.validate.field).int32.gte = 0];

  // Write buffer size in bytes
  int32 write_buffer_size = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### cookie_data.proto {#cookie_data}

**Path**: `gcommon/v1/web/cookie_data.proto` **Package**: `gcommon.v1.web` **Lines**: 45

**Messages** (1): `CookieData`

**Imports** (4):

- `gcommon/v1/common/cookie_same_site.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cookie_data.proto
// version: 1.1.0
// guid: a3854557-84b7-4173-8481-d69bf32fcbd0

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cookie_same_site.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// CookieData message definition.

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message CookieData {
  // Cookie name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cookie value
  string value = 2;

  // Cookie path
  string path = 3;

  // Cookie domain
  string domain = 4;

  // Expiration timestamp
  google.protobuf.Timestamp expires_at = 5;

  // Whether cookie is HTTP only
  bool http_only = 6;

  // Whether cookie is Secure
  bool secure = 7;

  // SameSite policy
  gcommon.v1.common.CookieSameSite same_site = 8;
}
```

---

### file_info.proto {#file_info}

**Path**: `gcommon/v1/web/file_info.proto` **Package**: `gcommon.v1.web` **Lines**: 34

**Messages** (1): `FileInfo`

**Imports** (4):

- `gcommon/v1/web/mime_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_info.proto
// version: 1.1.0
// guid: ee525bfe-ed87-4698-bf47-41bff85db277

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/mime_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// FileInfo message definition.
message FileInfo {
  // Full file path
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // File size in bytes
  int64 size_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // MIME type information
  MimeType mime_type = 3;

  // Last modified timestamp
  google.protobuf.Timestamp modified_at = 4;

  // Optional checksum of the file contents
  string checksum = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### file_metadata.proto {#file_metadata}

**Path**: `gcommon/v1/web/file_metadata.proto` **Package**: `gcommon.v1.web` **Lines**: 36

**Messages** (1): `FileMetadata`

**Imports** (4):

- `gcommon/v1/web/mime_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_metadata.proto
// version: 1.1.0
// guid: ac289d4b-2cc8-4cfb-a360-36eef7dba093

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/mime_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// FileMetadata message definition.
message FileMetadata {
  // File name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // File size in bytes
  int64 size_bytes = 2;

  // MIME type of the file
  MimeType mime_type = 3;

  // Optional checksum string
  string checksum = 4;

  // Last modification time
  google.protobuf.Timestamp modified_at = 5;
}
```

---

### file_upload.proto {#file_upload}

**Path**: `gcommon/v1/web/file_upload.proto` **Package**: `gcommon.v1.web` **Lines**: 32

**Messages** (1): `FileUpload`

**Imports** (3):

- `gcommon/v1/web/mime_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_upload.proto
// version: 1.1.0
// guid: 47f22269-7456-4237-b463-c287580f662d

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/mime_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// FileUpload message definition.
message FileUpload {
  // Name of the uploaded file
  string file_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Content type validation
  MimeType content_type = 2;

  // Raw file bytes
  bytes data = 3;

  // Destination path on server
  string destination = 4;
}
```

---

### handler_info.proto {#handler_info}

**Path**: `gcommon/v1/web/handler_info.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `HandlerInfo`

**Imports** (4):

- `gcommon/v1/web/handler_config.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handler_info.proto
// version: 1.1.0
// guid: ce840d82-a0a7-451a-ace7-062820511c9a

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/handler_config.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandlerInfo message definition.
message HandlerInfo {
  // Handler identifier
  string handler_id = 1;

  // Configuration for the handler
  HandlerConfig config = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

  // Last updated timestamp
  google.protobuf.Timestamp updated_at = 4;
}
```

---

### http_header.proto {#http_header}

**Path**: `gcommon/v1/web/http_header.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `HttpHeader`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_header.proto
// version: 1.0.0
// guid: 6a2d7cae-9978-46b7-951c-094945b969f9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HttpHeader message definition.
// HttpHeader represents a single HTTP header field.
message HttpHeader {
  // Header name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // One or more values for the header
  repeated string values = 2;
}
```

---

### middleware_info.proto {#middleware_info}

**Path**: `gcommon/v1/web/middleware_info.proto` **Package**: `gcommon.v1.web` **Lines**: 32

**Messages** (1): `MiddlewareInfo`

**Imports** (3):

- `gcommon/v1/common/middleware_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/middleware_info.proto
// version: 1.1.0
// guid: ddae7421-009f-4275-806a-9ff6d3270232

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/middleware_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// MiddlewareInfo message definition.
message MiddlewareInfo {
  // Middleware identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Middleware type
  gcommon.v1.common.MiddlewareType type = 2;

  // Execution order priority
  int32 order = 3;

  // Arbitrary metadata for middleware
  map<string, string> metadata = 4;
}
```

---

### mime_type.proto {#mime_type}

**Path**: `gcommon/v1/web/mime_type.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Messages** (1): `MimeType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/mime_type.proto
// version: 1.0.0
// guid: b600b818-5782-4f9d-ba1e-e6d3f0f23159

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// MimeType message definition.
// MimeType represents a content type with optional parameters.
message MimeType {
  // Primary type, e.g. "text"
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Subtype, e.g. "html"
  string subtype = 2 [(buf.validate.field).string.min_len = 1];

  // Optional parameters such as charset
  map<string, string> parameters = 3;
}
```

---

### performance_stats.proto {#performance_stats}

**Path**: `gcommon/v1/web/performance_stats.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `WebPerformanceStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/performance_stats.proto
// version: 1.1.0
// guid: 2ea24441-9142-4f94-b30e-9d8d07afa209

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// PerformanceStats message definition.
message WebPerformanceStats {
  // Total number of requests handled
  int64 request_count = 1 [(buf.validate.field).int64.gte = 0];

  // Average latency in milliseconds
  double average_latency_ms = 2 [(buf.validate.field).double.gte = 0.0];

  // Current active connections
  int32 active_connections = 3 [(buf.validate.field).int32.gte = 0];

  // Error rate percentage (0-100)
  double error_rate = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### route_info.proto {#route_info}

**Path**: `gcommon/v1/web/route_info.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `RouteInfo`

**Imports** (5):

- `gcommon/v1/common/route_type.proto`
- `gcommon/v1/web/route_config.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/route_info.proto
// version: 1.1.0
// guid: 8154bd31-51b0-4043-9a14-f0614adcd523

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/route_type.proto";
import "gcommon/v1/web/route_config.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RouteInfo message definition.
message RouteInfo {
  // Route configuration
  RouteConfig config = 1;

  // Type of route
  gcommon.v1.common.RouteType route_type = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 4;
}
```

---

### session_data.proto {#session_data}

**Path**: `gcommon/v1/web/session_data.proto` **Package**: `gcommon.v1.web` **Lines**: 48

**Messages** (1): `SessionData`

**Imports** (4):

- `gcommon/v1/common/web_session_state.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/session_data.proto
// version: 1.1.0
// guid: f93f7cc5-48c6-4b64-98d2-35549cf19b02

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/web_session_state.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SessionData message definition.
message SessionData {
  // Unique session identifier
  string session_id = 1;

  // User ID associated with the session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Current session state
  gcommon.v1.common.WebSessionState state = 3;

  // Session creation timestamp
  google.protobuf.Timestamp created_at = 4 [lazy = true, (buf.validate.field).required = true];

  // Last access timestamp
  google.protobuf.Timestamp last_access_at = 5 [lazy = true];

  // Session expiration timestamp
  google.protobuf.Timestamp expires_at = 6 [lazy = true];

  // Client IP address
  string ip_address = 7;

  // Client user agent
  string user_agent = 8;

  // Custom session metadata
  map<string, string> metadata = 9;
}
```

---

### template_data.proto {#template_data}

**Path**: `gcommon/v1/web/template_data.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Messages** (1): `TemplateData`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/template_data.proto
// version: 1.1.0
// guid: 31c5d8ac-caa3-4a45-816d-b831995e1757

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// TemplateData message definition.
message TemplateData {
  // Template name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Arbitrary context data
  google.protobuf.Any context = 2;

  // Template body source
  string template_body = 3;

  // Last compilation timestamp
  google.protobuf.Timestamp compiled_at = 4;
}
```

---

### url_path.proto {#url_path}

**Path**: `gcommon/v1/web/url_path.proto` **Package**: `gcommon.v1.web` **Lines**: 20

**Messages** (1): `UrlPath`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/url_path.proto
// version: 1.1.0
// guid: 265bd840-fba9-4930-ac69-55c9d3d55210

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UrlPath message definition.
message UrlPath {
  // Individual path segments
  repeated string segments = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### web.proto {#web}

**Path**: `gcommon/v1/web/web.proto` **Package**: `gcommon.v1.web` **Lines**: 38

**Messages** (1): `WebInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/web.proto
// version: 1.0.0
// guid: 5f6e7d8c-9b0a-1423-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Web represents basic web server information and metadata.
 * Contains fundamental web service configuration and status.
 */
message WebInfo {
  // Web server name/identifier
  string server_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Server version
  string version = 2;

  // Server start time
  google.protobuf.Timestamp started_at = 3;

  // Whether the server is accepting requests
  bool accepting_requests = 4;

  // Server port number
  int32 port = 5;
}
```

---

### websocket_info.proto {#websocket_info}

**Path**: `gcommon/v1/web/websocket_info.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebsocketInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/websocket_info.proto
// version: 1.1.0
// guid: 3ebae9bb-41c1-42db-aa71-8ef0660759d4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// WebsocketInfo message definition.
message WebsocketInfo {
  // Connection identifier
  string connection_id = 1 [(buf.validate.field).string.min_len = 1];

  // Client IP address
  string client_ip = 2 [(buf.validate.field).string.min_len = 1];

  // User agent string
  string user_agent = 3 [(buf.validate.field).string.min_len = 1];

  // Connection established timestamp
  google.protobuf.Timestamp connected_at = 4;
}
```

---

### websocket_message.proto {#websocket_message}

**Path**: `gcommon/v1/web/websocket_message.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebsocketMessage`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/websocket_message.proto
// version: 1.1.0
// guid: cba98cf1-43c2-4026-bcc0-779111b41ec1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// WebsocketMessage message definition.
message WebsocketMessage {
  // Connection identifier
  string connection_id = 1 [(buf.validate.field).string.min_len = 1];

  // Payload data
  bytes data = 2;

  // Optional message type label
  string message_type = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the message was sent
  google.protobuf.Timestamp sent_at = 4;
}
```

---

### add_middleware_request.proto {#add_middleware_request}

**Path**: `gcommon/v1/web/add_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `AddMiddlewareRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/add_middleware_request.proto
// version: 1.0.1
// guid: f3eee777-6416-43d6-9c51-7d0857359e6b

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * AddMiddlewareRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AddMiddlewareRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### add_middleware_response.proto {#add_middleware_response}

**Path**: `gcommon/v1/web/add_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `AddMiddlewareResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/add_middleware_response.proto
// version: 1.0.1
// guid: 7630a43f-ad62-483e-8e6e-3a8b8a24a8ee

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * AddMiddlewareResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AddMiddlewareResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### authenticate_request.proto {#authenticate_request}

**Path**: `gcommon/v1/web/authenticate_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthenticateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authenticate_request.proto
// version: 1.0.0
// guid: 94442c59-c156-4b84-b389-9423724c6635

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthenticateRequest request definition.
message WebAuthenticateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### authenticate_response.proto {#authenticate_response}

**Path**: `gcommon/v1/web/authenticate_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthenticateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authenticate_response.proto
// version: 1.0.0
// guid: f058366e-3b22-4c95-8be7-0ddf15eec85f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthenticateResponse response definition.
message WebAuthenticateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### authorize_request.proto {#authorize_request}

**Path**: `gcommon/v1/web/authorize_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthorizeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authorize_request.proto
// version: 1.0.0
// guid: 1582f475-35f6-43c9-ac19-74b29568fa64

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthorizeRequest request definition.
message WebAuthorizeRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### authorize_response.proto {#authorize_response}

**Path**: `gcommon/v1/web/authorize_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthorizeResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authorize_response.proto
// version: 1.0.0
// guid: df7cdfcb-6b3a-4991-a9e2-1b08a908570b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthorizeResponse response definition.
message WebAuthorizeResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### close_websocket_request.proto {#close_websocket_request}

**Path**: `gcommon/v1/web/close_websocket_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CloseWebsocketRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/close_websocket_request.proto
// version: 1.0.0
// guid: 43005508-aedc-4d2d-9b42-6fce6bd32ad9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CloseWebsocketRequest request definition.
message CloseWebsocketRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### close_websocket_response.proto {#close_websocket_response}

**Path**: `gcommon/v1/web/close_websocket_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CloseWebsocketResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/close_websocket_response.proto
// version: 1.0.0
// guid: eca486b9-3dd5-4720-9813-30a5b343bd8a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CloseWebsocketResponse response definition.
message CloseWebsocketResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_cookie_request.proto {#create_cookie_request}

**Path**: `gcommon/v1/web/create_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 55

**Messages** (1): `CreateCookieRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/same_site_policy.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_cookie_request.proto
// version: 1.2.0
// guid: 44838568-f1f6-44f1-b4a5-2299a815ccad

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/same_site_policy.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Request to create an HTTP cookie.
 * Used for session management and client state storage.
 */
message CreateCookieRequest {
  // Cookie name (required)
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cookie value
  string value = 2;

  // Cookie domain
  string domain = 3;

  // Cookie path
  string path = 4;

  // Cookie expiration time
  google.protobuf.Timestamp expires = 5;

  // Maximum age in seconds
  int32 max_age = 6;

  // Whether cookie is secure (HTTPS only)
  bool secure = 7;

  // Whether cookie is HTTP only
  bool http_only = 8;

  // Cookie SameSite attribute
  gcommon.v1.common.SameSitePolicy same_site = 9;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 10;
}
```

---

### create_cookie_response.proto {#create_cookie_response}

**Path**: `gcommon/v1/web/create_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_cookie_response.proto
// version: 1.0.0
// guid: 0d0254f8-1e8f-4646-817d-7ec57f25c88c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateCookieResponse response definition.
message CreateCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_server_request.proto {#create_server_request}

**Path**: `gcommon/v1/web/create_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `CreateServerRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_server_request.proto
// version: 1.0.1
// guid: a071056d-f27f-4932-aff8-57a2344955f2

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * CreateServerRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message CreateServerRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### create_server_response.proto {#create_server_response}

**Path**: `gcommon/v1/web/create_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `CreateServerResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_server_response.proto
// version: 1.0.1
// guid: e65e4983-3fb2-4098-b293-efc34aee92d8

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * CreateServerResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message CreateServerResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### create_session_request.proto {#create_session_request}

**Path**: `gcommon/v1/web/create_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 25

**Messages** (1): `WebCreateSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_session_request.proto
// version: 1.1.0
// guid: 1022341d-b551-43d4-b090-2354a82b624c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateSessionRequest request definition.
message WebCreateSessionRequest {
  // User ID for the new session
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional initial metadata
  map<string, string> metadata = 2;
}
```

---

### create_session_response.proto {#create_session_response}

**Path**: `gcommon/v1/web/create_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebCreateSessionResponse`

**Imports** (2):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_session_response.proto
// version: 1.1.1
// guid: 5b7bc14e-bb7d-4d0d-bd5b-c35bc5fb7bda

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateSessionResponse response definition.
message WebCreateSessionResponse {
  // Newly created session details
  SessionData session = 1;
}
```

---

### create_template_request.proto {#create_template_request}

**Path**: `gcommon/v1/web/create_template_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_template_request.proto
// version: 1.0.0
// guid: 0cb8a2eb-9d24-4b5c-9b3a-b66164b5ab50

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateTemplateRequest request definition.
message CreateTemplateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_template_response.proto {#create_template_response}

**Path**: `gcommon/v1/web/create_template_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_template_response.proto
// version: 1.0.0
// guid: 294f4744-3238-404c-94ec-85cb4b77bfbe

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateTemplateResponse response definition.
message CreateTemplateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_websocket_request.proto {#create_websocket_request}

**Path**: `gcommon/v1/web/create_websocket_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateWebsocketRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_websocket_request.proto
// version: 1.0.0
// guid: df288e0f-57af-4326-a2a7-91ff6b3ed38b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateWebsocketRequest request definition.
message CreateWebsocketRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_websocket_response.proto {#create_websocket_response}

**Path**: `gcommon/v1/web/create_websocket_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateWebsocketResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_websocket_response.proto
// version: 1.0.0
// guid: e46f3fe0-b2cb-4d13-982a-4a28a59a2025

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateWebsocketResponse response definition.
message CreateWebsocketResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_cookie_request.proto {#delete_cookie_request}

**Path**: `gcommon/v1/web/delete_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteCookieRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_cookie_request.proto
// version: 1.0.0
// guid: 704e1ea8-b8a8-4c45-9a2f-3571aa92021e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteCookieRequest request definition.
message DeleteCookieRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_cookie_response.proto {#delete_cookie_response}

**Path**: `gcommon/v1/web/delete_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_cookie_response.proto
// version: 1.0.0
// guid: 2b9f0298-3825-4e48-8606-dae4d44c0b9c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteCookieResponse response definition.
message DeleteCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_file_request.proto {#delete_file_request}

**Path**: `gcommon/v1/web/delete_file_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_file_request.proto
// version: 1.0.0
// guid: d13d91f6-e28f-4932-bd69-254f9ab926cf

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteFileRequest request definition.
message DeleteFileRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_file_response.proto {#delete_file_response}

**Path**: `gcommon/v1/web/delete_file_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteFileResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_file_response.proto
// version: 1.0.0
// guid: ece03faf-72a0-4c28-9084-8636a30178d0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteFileResponse response definition.
message DeleteFileResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_session_request.proto {#delete_session_request}

**Path**: `gcommon/v1/web/delete_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 20

**Messages** (1): `WebDeleteSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_session_request.proto
// version: 1.1.0
// guid: 90ce1e00-4c38-47bf-b246-fba60817030a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteSessionRequest request definition.
message WebDeleteSessionRequest {
  // Identifier of the session to delete
  string session_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_session_response.proto {#delete_session_response}

**Path**: `gcommon/v1/web/delete_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 18

**Messages** (1): `WebDeleteSessionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_session_response.proto
// version: 1.1.1
// guid: 4115c974-f373-4e67-aeb0-fff852ec685a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteSessionResponse response definition.
message WebDeleteSessionResponse {
  // Indicates if the session was deleted
  bool success = 1;
}
```

---

### delete_template_request.proto {#delete_template_request}

**Path**: `gcommon/v1/web/delete_template_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_template_request.proto
// version: 1.0.0
// guid: 77e6e070-8d45-407c-bf0d-4fa8e59286c9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteTemplateRequest request definition.
message DeleteTemplateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_template_response.proto {#delete_template_response}

**Path**: `gcommon/v1/web/delete_template_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_template_response.proto
// version: 1.0.0
// guid: 694ea8d5-14d0-4199-ba28-c703229f2782

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteTemplateResponse response definition.
message DeleteTemplateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### download_file_request.proto {#download_file_request}

**Path**: `gcommon/v1/web/download_file_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DownloadFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/download_file_request.proto
// version: 1.0.0
// guid: 9505fac6-9597-4f3f-9adf-caff8184f860

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DownloadFileRequest request definition.
message DownloadFileRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### download_file_response.proto {#download_file_response}

**Path**: `gcommon/v1/web/download_file_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DownloadFileResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/download_file_response.proto
// version: 1.0.0
// guid: ad823437-e5e1-4b0c-afb4-9eea7f74a97f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DownloadFileResponse response definition.
message DownloadFileResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### flush_cache_request.proto {#flush_cache_request}

**Path**: `gcommon/v1/web/flush_cache_request.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `FlushCacheRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/flush_cache_request.proto
// version: 1.0.0
// guid: mno78901-2345-6789-abcd-ef1234567890

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message FlushCacheRequest {
  // Optional namespace to flush (if empty, flushes all)
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### flush_cache_response.proto {#flush_cache_response}

**Path**: `gcommon/v1/web/flush_cache_response.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `FlushCacheResponse`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/flush_cache_response.proto
// version: 1.0.0
// guid: pqr01234-5678-9abc-def0-123456789012

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message FlushCacheResponse {
  // Whether the flush was successful
  bool success = 1;

  // Number of entries flushed
  int64 entries_flushed = 2 [(buf.validate.field).int64.gte = 0];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### generate_csrf_token_request.proto {#generate_csrf_token_request}

**Path**: `gcommon/v1/web/generate_csrf_token_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GenerateCsrfTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/generate_csrf_token_request.proto
// version: 1.0.0
// guid: b05fa822-c009-4975-ac54-ef39dbdcaa7e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GenerateCsrfTokenRequest request definition.
message GenerateCsrfTokenRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### generate_csrf_token_response.proto {#generate_csrf_token_response}

**Path**: `gcommon/v1/web/generate_csrf_token_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GenerateCsrfTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/generate_csrf_token_response.proto
// version: 1.0.0
// guid: 2883e71c-133f-4b82-aadf-9883eb41bb68

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GenerateCsrfTokenResponse response definition.
message GenerateCsrfTokenResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_access_logs_request.proto {#get_access_logs_request}

**Path**: `gcommon/v1/web/get_access_logs_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetAccessLogsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_access_logs_request.proto
// version: 1.0.1
// guid: b1ae7686-f402-48c3-a4cf-a89cf32e9fe3

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetAccessLogsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetAccessLogsRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### get_access_logs_response.proto {#get_access_logs_response}

**Path**: `gcommon/v1/web/get_access_logs_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetAccessLogsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_access_logs_response.proto
// version: 1.0.1
// guid: d3a99c97-12b6-4158-b9b9-339b0aaa8d87

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetAccessLogsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetAccessLogsResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_cookie_request.proto {#get_cookie_request}

**Path**: `gcommon/v1/web/get_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCookieRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cookie_request.proto
// version: 1.0.0
// guid: c813599e-921b-4476-a0ce-e43beac01bdb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCookieRequest request definition.
message GetCookieRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_cookie_response.proto {#get_cookie_response}

**Path**: `gcommon/v1/web/get_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cookie_response.proto
// version: 1.0.0
// guid: 9408a9d0-e0d9-4b42-97c3-bb662f1a5990

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCookieResponse response definition.
message GetCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_file_info_request.proto {#get_file_info_request}

**Path**: `gcommon/v1/web/get_file_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetFileInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_file_info_request.proto
// version: 1.0.0
// guid: cf3df7e0-3738-456e-9082-d5ccd898b372

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetFileInfoRequest request definition.
message GetFileInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_file_info_response.proto {#get_file_info_response}

**Path**: `gcommon/v1/web/get_file_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetFileInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_file_info_response.proto
// version: 1.0.0
// guid: c49bbb1e-7f94-4a6d-84e5-e9517b988719

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetFileInfoResponse response definition.
message GetFileInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_handler_info_request.proto {#get_handler_info_request}

**Path**: `gcommon/v1/web/get_handler_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetHandlerInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_handler_info_request.proto
// version: 1.0.0
// guid: 8e46bc43-d8f7-4053-bb73-4e458022efb6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetHandlerInfoRequest request definition.
message GetHandlerInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_handler_info_response.proto {#get_handler_info_response}

**Path**: `gcommon/v1/web/get_handler_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetHandlerInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_handler_info_response.proto
// version: 1.0.0
// guid: d6203aa9-40d1-47d9-8c6d-ea2d7cf3c76e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetHandlerInfoResponse response definition.
message GetHandlerInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_metrics_request.proto {#get_metrics_request}

**Path**: `gcommon/v1/web/get_metrics_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebGetMetricsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_metrics_request.proto
// version: 1.0.0
// guid: 21aad446-24e7-442f-a61f-0287b7742589

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMetricsRequest request definition.
message WebGetMetricsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_metrics_response.proto {#get_metrics_response}

**Path**: `gcommon/v1/web/get_metrics_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebGetMetricsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_metrics_response.proto
// version: 1.0.0
// guid: d42faed3-d602-4066-a445-01c6f1bf8448

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMetricsResponse response definition.
message WebGetMetricsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_middleware_info_request.proto {#get_middleware_info_request}

**Path**: `gcommon/v1/web/get_middleware_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetMiddlewareInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_middleware_info_request.proto
// version: 1.0.0
// guid: c8c3314e-63ab-46b2-a217-5c81a2f55eb0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMiddlewareInfoRequest request definition.
message GetMiddlewareInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_middleware_info_response.proto {#get_middleware_info_response}

**Path**: `gcommon/v1/web/get_middleware_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetMiddlewareInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_middleware_info_response.proto
// version: 1.0.0
// guid: 46941911-33dc-4735-8f43-e834fa94e935

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMiddlewareInfoResponse response definition.
message GetMiddlewareInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_performance_stats_request.proto {#get_performance_stats_request}

**Path**: `gcommon/v1/web/get_performance_stats_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetPerformanceStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_performance_stats_request.proto
// version: 1.0.0
// guid: 2858eba1-31b0-47f0-9d29-91c78943323b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetPerformanceStatsRequest request definition.
message GetPerformanceStatsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_performance_stats_response.proto {#get_performance_stats_response}

**Path**: `gcommon/v1/web/get_performance_stats_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetPerformanceStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_performance_stats_response.proto
// version: 1.0.0
// guid: ecadd1ec-a5eb-4813-a0c7-055cfc58c7be

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetPerformanceStatsResponse response definition.
message GetPerformanceStatsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_route_info_request.proto {#get_route_info_request}

**Path**: `gcommon/v1/web/get_route_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetRouteInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_info_request.proto
// version: 1.0.0
// guid: bc9c9890-0ee4-4a5f-b0e9-1f06ae76801c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetRouteInfoRequest request definition.
message GetRouteInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_route_info_response.proto {#get_route_info_response}

**Path**: `gcommon/v1/web/get_route_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetRouteInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_info_response.proto
// version: 1.0.0
// guid: 8717580f-b835-4cf1-97f8-afc41daf8ed4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetRouteInfoResponse response definition.
message GetRouteInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_route_metrics_request.proto {#get_route_metrics_request}

**Path**: `gcommon/v1/web/get_route_metrics_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetRouteMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_metrics_request.proto
// version: 1.0.1
// guid: fd25fe7a-1f87-4979-8502-8ff4b7022e24

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetRouteMetricsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetRouteMetricsRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### get_route_metrics_response.proto {#get_route_metrics_response}

**Path**: `gcommon/v1/web/get_route_metrics_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetRouteMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_metrics_response.proto
// version: 1.0.1
// guid: a14b318a-9397-452e-8f29-201aa145aa19

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetRouteMetricsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetRouteMetricsResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_server_health_request.proto {#get_server_health_request}

**Path**: `gcommon/v1/web/get_server_health_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerHealthRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_health_request.proto
// version: 1.0.1
// guid: 150fcfd0-33d0-453e-a628-70235d0d760d

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetServerHealthRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerHealthRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### get_server_health_response.proto {#get_server_health_response}

**Path**: `gcommon/v1/web/get_server_health_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerHealthResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_health_response.proto
// version: 1.0.1
// guid: 3b792629-d4ac-4821-8ab0-badba4ad3aea

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetServerHealthResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerHealthResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_server_logs_request.proto {#get_server_logs_request}

**Path**: `gcommon/v1/web/get_server_logs_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerLogsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_logs_request.proto
// version: 1.0.1
// guid: 8e8d56e9-af3b-4205-bab3-d528f6528104

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetServerLogsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerLogsRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### get_server_logs_response.proto {#get_server_logs_response}

**Path**: `gcommon/v1/web/get_server_logs_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerLogsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_logs_response.proto
// version: 1.0.1
// guid: 2bece2cb-e346-41b9-8e2b-2bdbbbe4c94f

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetServerLogsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerLogsResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_server_metrics_request.proto {#get_server_metrics_request}

**Path**: `gcommon/v1/web/get_server_metrics_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_metrics_request.proto
// version: 1.0.1
// guid: 3f87be3d-9370-43a0-88fc-13d5eb9eb37a

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetServerMetricsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerMetricsRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### get_server_metrics_response.proto {#get_server_metrics_response}

**Path**: `gcommon/v1/web/get_server_metrics_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_metrics_response.proto
// version: 1.0.1
// guid: c7d26642-5c77-4ba5-b891-5876066cfaba

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetServerMetricsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerMetricsResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_server_status_request.proto {#get_server_status_request}

**Path**: `gcommon/v1/web/get_server_status_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerStatusRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_status_request.proto
// version: 1.0.0
// guid: 589c81b7-a311-4da5-9604-ece349fc6e55

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerStatusRequest request definition.
message GetServerStatusRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_server_status_response.proto {#get_server_status_response}

**Path**: `gcommon/v1/web/get_server_status_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerStatusResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_status_response.proto
// version: 1.0.0
// guid: 3cb9f0ee-d816-469a-89f1-0486c03c9f3a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerStatusResponse response definition.
message GetServerStatusResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_session_request.proto {#get_session_request}

**Path**: `gcommon/v1/web/get_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 20

**Messages** (1): `WebGetSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_session_request.proto
// version: 1.1.0
// guid: 5ab16058-a2a8-463c-b101-b1f24df275ef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSessionRequest request definition.
message WebGetSessionRequest {
  // Identifier of the session to retrieve
  string session_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_session_response.proto {#get_session_response}

**Path**: `gcommon/v1/web/get_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebGetSessionResponse`

**Imports** (2):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_session_response.proto
// version: 1.1.1
// guid: 97fcede8-5243-4901-b423-41a0723fb0c7

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSessionResponse response definition.
message WebGetSessionResponse {
  // Retrieved session data
  SessionData session = 1;
}
```

---

### get_ssl_certificate_info_request.proto {#get_ssl_certificate_info_request}

**Path**: `gcommon/v1/web/get_ssl_certificate_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetSSLCertificateInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_ssl_certificate_info_request.proto
// version: 1.0.1
// guid: dc573011-0a3c-48ac-9de4-3a7718171101

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetSSLCertificateInfoRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetSSLCertificateInfoRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### get_ssl_certificate_info_response.proto {#get_ssl_certificate_info_response}

**Path**: `gcommon/v1/web/get_ssl_certificate_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetSSLCertificateInfoResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_ssl_certificate_info_response.proto
// version: 1.0.1
// guid: 9ffed0bc-f94b-47a9-8a07-7e01d998e746

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * GetSSLCertificateInfoResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetSSLCertificateInfoResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### get_template_info_request.proto {#get_template_info_request}

**Path**: `gcommon/v1/web/get_template_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetTemplateInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_template_info_request.proto
// version: 1.0.0
// guid: 0660a509-2a17-4efb-be93-9712e8b2c84e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetTemplateInfoRequest request definition.
message GetTemplateInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_template_info_response.proto {#get_template_info_response}

**Path**: `gcommon/v1/web/get_template_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetTemplateInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_template_info_response.proto
// version: 1.0.0
// guid: e1cc4547-9204-48a5-84a3-3c7526d71494

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetTemplateInfoResponse response definition.
message GetTemplateInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_websocket_info_request.proto {#get_websocket_info_request}

**Path**: `gcommon/v1/web/get_websocket_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetWebsocketInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_websocket_info_request.proto
// version: 1.0.0
// guid: 48f87988-451a-453b-9f51-2c7175112c25

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetWebsocketInfoRequest request definition.
message GetWebsocketInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_websocket_info_response.proto {#get_websocket_info_response}

**Path**: `gcommon/v1/web/get_websocket_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetWebsocketInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_websocket_info_response.proto
// version: 1.0.0
// guid: 147168a6-ba00-4881-8ddd-dd52c3af7198

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetWebsocketInfoResponse response definition.
message GetWebsocketInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### handle_request.proto {#handle_request}

**Path**: `gcommon/v1/web/handle_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `HandleRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_request.proto
// version: 1.0.0
// guid: 50315b83-99de-4058-b883-61ebfa2b47a8

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandleRequest request definition.
message HandleRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### handle_request_request.proto {#handle_request_request}

**Path**: `gcommon/v1/web/handle_request_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `HandleRequestRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_request_request.proto
// version: 1.0.1
// guid: 0af45f43-528e-4f14-a668-eebf5ae2d975

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * HandleRequestRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HandleRequestRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### handle_request_response.proto {#handle_request_response}

**Path**: `gcommon/v1/web/handle_request_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `HandleRequestResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_request_response.proto
// version: 1.0.1
// guid: c75ed356-c467-40db-ac2c-529e7b956802

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * HandleRequestResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HandleRequestResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### handle_response.proto {#handle_response}

**Path**: `gcommon/v1/web/handle_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `HandleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_response.proto
// version: 1.0.0
// guid: 54494647-eae8-4100-9c64-809b55fe043a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandleResponse response definition.
message HandleResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/web/health_check_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebHealthCheckRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/health_check_request.proto
// version: 1.0.1
// guid: 08748b61-ccf0-4bfe-bfc6-ad2778f3959c
// HealthCheckRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message WebHealthCheckRequest {
  // Request metadata for the HTTP server.
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/web/health_check_response.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Messages** (1): `WebHealthCheckResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/health_check_response.proto
// version: 1.0.1
// guid: abec6322-3426-4dde-8a30-3afe453d1650

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HealthCheckResponse response definition.
message WebHealthCheckResponse {
  // Web server health status.
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Time taken to respond to the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Error details if the server is unhealthy.
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### http_request.proto {#http_request}

**Path**: `gcommon/v1/web/http_request.proto` **Package**: `gcommon.v1.web` **Lines**: 175

**Messages** (1): `HttpRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_request.proto
// version: 1.0.0
// guid: fb9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * HttpRequest represents an HTTP request for processing by web services.
 * Captures all essential HTTP request information including headers,
 * body, and metadata for service mesh and proxy use cases.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HttpRequest {
  // Required fields (1-10)

  /**
   * HTTP method (GET, POST, PUT, DELETE, etc.).
   */
  string method = 1;

  /**
   * Request URL including scheme, host, path, and query parameters.
   * Example: "https://api.example.com/v1/users?limit=10"
   */
  string url = 2;

  /**
   * HTTP protocol version (e.g., "HTTP/1.1", "HTTP/2", "HTTP/3").
   */
  string protocol_version = 3;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * HTTP headers as key-value pairs.
   * Includes standard headers like Content-Type, Authorization, etc.
   */
  map<string, string> headers = 12;

  /**
   * Request body/payload data.
   * Can contain any content type (JSON, XML, binary, etc.).
   */
  google.protobuf.Any body = 13;

  /**
   * Query parameters extracted from the URL.
   * Provided separately for easier access.
   */
  map<string, string> query_params = 14;

  /**
   * Path parameters extracted from the URL pattern.
   * Example: For /users/{user_id}, would contain {"user_id": "123"}
   */
  map<string, string> path_params = 15;

  /**
   * Cookies sent with the request.
   */
  map<string, string> cookies = 16;

  /**
   * Client IP address (original or from proxy headers).
   */
  string client_ip = 17;

  /**
   * User agent string from the client.
   */
  string user_agent = 18;

  /**
   * Referrer URL (if present).
   */
  string referrer = 19;

  /**
   * Content length in bytes.
   */
  int64 content_length = 20;

  /**
   * Content type of the request body.
   */
  string content_type = 21;

  /**
   * Accept header value indicating preferred response types.
   */
  string accept = 22;

  /**
   * Accept-Language header for internationalization.
   */
  string accept_language = 23;

  /**
   * Accept-Encoding header for compression negotiation.
   */
  string accept_encoding = 24;

  /**
   * Authorization header value.
   */
  string authorization = 25;

  /**
   * Request ID for tracking and correlation.
   * May be generated by load balancers or API gateways.
   */
  string request_id = 26;

  /**
   * Session ID if the request is part of a user session.
   */
  string session_id = 27;

  /**
   * Target service name for routing in service mesh.
   */
  string target_service = 28;

  /**
   * Target service version for version-specific routing.
   */
  string target_version = 29;

  /**
   * Request timeout in milliseconds.
   */
  int64 timeout_ms = 30;

  /**
   * Whether the request expects a streaming response.
   */
  bool streaming = 31;

  /**
   * Whether the connection should be kept alive.
   */
  bool keep_alive = 32;

  // Timestamps (51-60)

  /**
   * When the request was received by the first proxy/gateway.
   */
  google.protobuf.Timestamp received_at = 51;

  /**
   * When the request was created/initiated by the client.
   */
  google.protobuf.Timestamp created_at = 52 [ (buf.validate.field).required = true ];
}
```

---

### http_response.proto {#http_response}

**Path**: `gcommon/v1/web/http_response.proto` **Package**: `gcommon.v1.web` **Lines**: 193

**Messages** (1): `HttpResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_response.proto
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * HttpResponse represents an HTTP response from web services.
 * Captures all essential HTTP response information including status,
 * headers, body, and metadata for service mesh and proxy use cases.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HttpResponse {
  // Required fields (1-10)

  /**
   * HTTP status code (200, 404, 500, etc.).
   */
  int32 status_code = 1;

  /**
   * HTTP status message/reason phrase (OK, Not Found, Internal Server Error, etc.).
   */
  string status_message = 2;

  /**
   * HTTP protocol version used for the response.
   */
  string protocol_version = 3;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * HTTP response headers as key-value pairs.
   * Includes standard headers like Content-Type, Cache-Control, etc.
   */
  map<string, string> headers = 12;

  /**
   * Response body/payload data.
   * Can contain any content type (JSON, XML, HTML, binary, etc.).
   */
  google.protobuf.Any body = 13;

  /**
   * Cookies to be set in the client.
   */
  map<string, string> cookies = 14;

  /**
   * Content length in bytes.
   */
  int64 content_length = 15;

  /**
   * Content type of the response body.
   */
  string content_type = 16;

  /**
   * Content encoding (gzip, deflate, etc.).
   */
  string content_encoding = 17;

  /**
   * Cache-Control header value.
   */
  string cache_control = 18;

  /**
   * ETag header for caching and conditional requests.
   */
  string etag = 19;

  /**
   * Location header for redirects.
   */
  string location = 20;

  /**
   * Server header identifying the server software.
   */
  string server = 21;

  /**
   * CORS Access-Control-Allow-Origin header.
   */
  string access_control_allow_origin = 22;

  /**
   * CORS Access-Control-Allow-Methods header.
   */
  string access_control_allow_methods = 23;

  /**
   * CORS Access-Control-Allow-Headers header.
   */
  string access_control_allow_headers = 24;

  /**
   * Request ID that was processed (for correlation).
   */
  string request_id = 25;

  /**
   * Service name that generated this response.
   */
  string service_name = 26 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * Service version that generated this response.
   */
  string service_version = 27;

  /**
   * Response processing time in milliseconds.
   */
  int64 processing_time_ms = 28;

  /**
   * Whether the response was served from cache.
   */
  bool served_from_cache = 29;

  /**
   * Whether the response is being streamed.
   */
  bool streaming = 30;

  /**
   * Whether the connection will be kept alive.
   */
  bool keep_alive = 31;

  /**
   * Whether the response was compressed.
   */
  bool compressed = 32;

  /**
   * Compression ratio if compressed (0.0-1.0).
   */
  float compression_ratio = 33;

  // Status and error fields (61-70)

  /**
   * Error information if the response represents an error
   * or if there were issues generating the response.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * When response generation started.
   */
  google.protobuf.Timestamp processing_started_at = 51;

  /**
   * When the response was generated.
   */
  google.protobuf.Timestamp generated_at = 52;

  /**
   * When the response was sent to the client.
   */
  google.protobuf.Timestamp sent_at = 53;
}
```

---

### list_cookies_request.proto {#list_cookies_request}

**Path**: `gcommon/v1/web/list_cookies_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListCookiesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_cookies_request.proto
// version: 1.0.0
// guid: b31f8f02-8e3b-4c2c-8094-5e991dabb601

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListCookiesRequest request definition.
message ListCookiesRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_cookies_response.proto {#list_cookies_response}

**Path**: `gcommon/v1/web/list_cookies_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListCookiesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_cookies_response.proto
// version: 1.0.0
// guid: af6c455c-4937-4d9b-a355-2124c8e24b91

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListCookiesResponse response definition.
message ListCookiesResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_files_request.proto {#list_files_request}

**Path**: `gcommon/v1/web/list_files_request.proto` **Package**: `gcommon.v1.web` **Lines**: 46

**Messages** (1): `ListFilesRequest`

**Imports** (4):

- `gcommon/v1/common/file_sort_order.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_files_request.proto
// version: 1.2.0
// guid: 69d44c54-6e03-4313-a56c-2df3041206f8

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/file_sort_order.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Request to list files in a directory.
 * Used for static file serving and directory browsing.
 */
message ListFilesRequest {
  // Directory path to list files from
  string directory_path = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to include subdirectories recursively
  bool recursive = 2;

  // File pattern filter (glob-style)
  string pattern = 3 [(buf.validate.field).string.min_len = 1];

  // Maximum number of files to return
  int32 limit = 4 [(buf.validate.field).int32.gte = 0];

  // Pagination offset
  int32 offset = 5 [(buf.validate.field).int32.gte = 0];

  // Whether to include hidden files (starting with .)
  bool include_hidden = 6;

  // Sort order for the files
  gcommon.v1.common.FileSortOrder sort_order = 7;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 8;
}
```

---

### list_files_response.proto {#list_files_response}

**Path**: `gcommon/v1/web/list_files_response.proto` **Package**: `gcommon.v1.web` **Lines**: 37

**Messages** (1): `ListFilesResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/web/file_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_files_response.proto
// version: 1.1.0
// guid: 0ee5d62d-df69-4b40-a4ea-a36fb6e16147

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/web/file_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Response containing a list of files from a directory or file system.
 * Used for file browsing and management operations.
 */
message ListFilesResponse {
  // List of files and directories
  repeated FileInfo files = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of files (may be larger than returned list if paginated)
  int64 total_count = 2 [(buf.validate.field).int64.gte = 0];

  // Token for next page (if paginated)
  string next_page_token = 3 [(buf.validate.field).string.min_len = 1];

  // Whether there are more results
  bool has_more = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}
```

---

### list_handlers_request.proto {#list_handlers_request}

**Path**: `gcommon/v1/web/list_handlers_request.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `ListHandlersRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_handlers_request.proto
// version: 1.1.0
// guid: 5141d082-9a7d-4518-bc9a-3bdf2aca716c

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Request to list registered HTTP handlers.
 * Used for route discovery and management.
 */
message ListHandlersRequest {
  // Filter by HTTP method (GET, POST, etc.)
  string method_filter = 1 [(buf.validate.field).string.min_len = 1];

  // Filter by path pattern
  string path_filter = 2 [(buf.validate.field).string.min_len = 1];

  // Whether to include middleware information
  bool include_middleware = 3;

  // Maximum number of handlers to return
  int32 limit = 4 [(buf.validate.field).int32.gte = 0];

  // Pagination offset
  int32 offset = 5 [(buf.validate.field).int32.gte = 0];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}
```

---

### list_handlers_response.proto {#list_handlers_response}

**Path**: `gcommon/v1/web/list_handlers_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListHandlersResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_handlers_response.proto
// version: 1.0.0
// guid: 0dafdb52-5ffd-4e3f-a17a-9527935385b0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListHandlersResponse response definition.
message ListHandlersResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_middleware_request.proto {#list_middleware_request}

**Path**: `gcommon/v1/web/list_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 35

**Messages** (1): `ListMiddlewareRequest`

**Imports** (5):

- `gcommon/v1/common/middleware_type.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_middleware_request.proto
// version: 1.1.0
// guid: 0717a6fd-6194-47c2-a17e-4cb18eac5bba

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/middleware_type.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListMiddlewareRequest request definition.
message ListMiddlewareRequest {
  // Server identifier
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Filter by middleware type
  gcommon.v1.common.MiddlewareType type = 2;

  // Filter by enabled state
  bool enabled = 3;

  // Pagination options
  gcommon.v1.common.Pagination pagination = 4;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### list_middleware_response.proto {#list_middleware_response}

**Path**: `gcommon/v1/web/list_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `ListMiddlewareResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/web/middleware_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_middleware_response.proto
// version: 1.1.0
// guid: 340d48d9-09d3-4bef-bafb-c16741471339

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/web/middleware_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListMiddlewareResponse response definition.
message ListMiddlewareResponse {
  // Middleware information
  repeated MiddlewareInfo middleware = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination details
  gcommon.v1.common.Pagination pagination = 2;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}
```

---

### list_routes_request.proto {#list_routes_request}

**Path**: `gcommon/v1/web/list_routes_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListRoutesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_routes_request.proto
// version: 1.0.0
// guid: aae7a362-705b-4f59-b285-58b5df10536d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListRoutesRequest request definition.
message ListRoutesRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_routes_response.proto {#list_routes_response}

**Path**: `gcommon/v1/web/list_routes_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListRoutesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_routes_response.proto
// version: 1.0.0
// guid: 47f1c54d-cebd-43eb-a358-7c79ccffcbf3

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListRoutesResponse response definition.
message ListRoutesResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_servers_request.proto {#list_servers_request}

**Path**: `gcommon/v1/web/list_servers_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ListServersRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_servers_request.proto
// version: 1.0.1
// guid: 1b601e51-740d-448e-b1cf-ca06a0180bee

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ListServersRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListServersRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### list_servers_response.proto {#list_servers_response}

**Path**: `gcommon/v1/web/list_servers_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ListServersResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_servers_response.proto
// version: 1.0.1
// guid: 794ce93d-bcc4-4324-a6d6-867f13442500

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ListServersResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListServersResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### list_sessions_request.proto {#list_sessions_request}

**Path**: `gcommon/v1/web/list_sessions_request.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `WebListSessionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_sessions_request.proto
// version: 1.1.0
// guid: a6c1c53c-e5dd-4cbc-9a88-357c8c22e179

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListSessionsRequest request definition.
message WebListSessionsRequest {
  // Filter sessions by user ID (optional)
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### list_sessions_response.proto {#list_sessions_response}

**Path**: `gcommon/v1/web/list_sessions_response.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Messages** (1): `WebListSessionsResponse`

**Imports** (3):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_sessions_response.proto
// version: 1.1.0
// guid: f9b7c78a-576f-4603-9a83-de8d0abb2341

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListSessionsResponse response definition.
message WebListSessionsResponse {
  // List of active sessions
  repeated SessionData sessions = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### list_templates_request.proto {#list_templates_request}

**Path**: `gcommon/v1/web/list_templates_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListTemplatesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_templates_request.proto
// version: 1.0.0
// guid: 17a404df-9dc4-4ee0-b848-9acd1d114fac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListTemplatesRequest request definition.
message ListTemplatesRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_templates_response.proto {#list_templates_response}

**Path**: `gcommon/v1/web/list_templates_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListTemplatesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_templates_response.proto
// version: 1.0.0
// guid: f71c982a-072a-4971-b28b-8aa39775d4cc

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListTemplatesResponse response definition.
message ListTemplatesResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_websockets_request.proto {#list_websockets_request}

**Path**: `gcommon/v1/web/list_websockets_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListWebsocketsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_websockets_request.proto
// version: 1.0.0
// guid: 4e624d8b-c0a8-4db1-a31a-1b7edabb3b76

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListWebsocketsRequest request definition.
message ListWebsocketsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_websockets_response.proto {#list_websockets_response}

**Path**: `gcommon/v1/web/list_websockets_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListWebsocketsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_websockets_response.proto
// version: 1.0.0
// guid: 1dd3b983-0837-4026-bca1-57e896d2d1fb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListWebsocketsResponse response definition.
message ListWebsocketsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_handler_request.proto {#register_handler_request}

**Path**: `gcommon/v1/web/register_handler_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterHandlerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_handler_request.proto
// version: 1.0.0
// guid: 808ab079-268c-49db-be80-37f91f8c9f7e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterHandlerRequest request definition.
message RegisterHandlerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_handler_response.proto {#register_handler_response}

**Path**: `gcommon/v1/web/register_handler_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterHandlerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_handler_response.proto
// version: 1.0.0
// guid: a59897f6-9cf0-48f8-8117-621aea3b60e0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterHandlerResponse response definition.
message RegisterHandlerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_middleware_request.proto {#register_middleware_request}

**Path**: `gcommon/v1/web/register_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Messages** (1): `RegisterMiddlewareRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/middleware_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_middleware_request.proto
// version: 1.1.0
// guid: c136f229-3eee-476f-87b9-6417ec8bb8b0
// RegisterMiddlewareRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/middleware_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message RegisterMiddlewareRequest {
  // Target server identifier
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Middleware configuration
  MiddlewareConfig middleware = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### register_middleware_response.proto {#register_middleware_response}

**Path**: `gcommon/v1/web/register_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `RegisterMiddlewareResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/web/middleware_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_middleware_response.proto
// version: 1.1.1
// guid: 759e7f49-492f-4cf6-ae71-bfcc4f96aa83

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/web/middleware_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterMiddlewareResponse response definition.
message RegisterMiddlewareResponse {
  // Operation success flag
  bool success = 1;

  // Details about the registered middleware
  MiddlewareInfo middleware = 2;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}
```

---

### register_route_request.proto {#register_route_request}

**Path**: `gcommon/v1/web/register_route_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterRouteRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_route_request.proto
// version: 1.0.0
// guid: 0c8be2b5-29b4-4207-a6a3-91d9c03312fe

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterRouteRequest request definition.
message RegisterRouteRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_route_response.proto {#register_route_response}

**Path**: `gcommon/v1/web/register_route_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterRouteResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_route_response.proto
// version: 1.0.0
// guid: d4348084-2633-450e-b54d-876af3f04908

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterRouteResponse response definition.
message RegisterRouteResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### remove_middleware_request.proto {#remove_middleware_request}

**Path**: `gcommon/v1/web/remove_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `RemoveMiddlewareRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/remove_middleware_request.proto
// version: 1.0.1
// guid: 8a7398c4-58cc-47b4-a4db-e53da72f74d5

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * RemoveMiddlewareRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message RemoveMiddlewareRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### remove_middleware_response.proto {#remove_middleware_response}

**Path**: `gcommon/v1/web/remove_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `RemoveMiddlewareResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/remove_middleware_response.proto
// version: 1.0.1
// guid: 6b5a3ac2-61d8-478d-874b-c0fcbb4eceed

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * RemoveMiddlewareResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message RemoveMiddlewareResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### render_template_request.proto {#render_template_request}

**Path**: `gcommon/v1/web/render_template_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RenderTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/render_template_request.proto
// version: 1.0.0
// guid: 7af6bf58-6fbd-443a-a1b4-bbff1986136c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RenderTemplateRequest request definition.
message RenderTemplateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### render_template_response.proto {#render_template_response}

**Path**: `gcommon/v1/web/render_template_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RenderTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/render_template_response.proto
// version: 1.0.0
// guid: 97e5b67b-3c0e-46dc-9e4b-66964408d78e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RenderTemplateResponse response definition.
message RenderTemplateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### reset_stats_request.proto {#reset_stats_request}

**Path**: `gcommon/v1/web/reset_stats_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ResetStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reset_stats_request.proto
// version: 1.0.0
// guid: 489cfa57-6202-40a6-bdff-a76a1f55fa1d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ResetStatsRequest request definition.
message ResetStatsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### reset_stats_response.proto {#reset_stats_response}

**Path**: `gcommon/v1/web/reset_stats_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ResetStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reset_stats_response.proto
// version: 1.0.0
// guid: 1d37d4bf-fa7b-4794-aa70-4d3b11142625

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ResetStatsResponse response definition.
message ResetStatsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### restart_server_request.proto {#restart_server_request}

**Path**: `gcommon/v1/web/restart_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RestartServerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/restart_server_request.proto
// version: 1.0.0
// guid: 9fc26a42-b6e1-4d63-a78a-24fa09be9abb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RestartServerRequest request definition.
message RestartServerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### restart_server_response.proto {#restart_server_response}

**Path**: `gcommon/v1/web/restart_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RestartServerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/restart_server_response.proto
// version: 1.0.0
// guid: a53bc58d-9a8b-490a-b3c7-f33025aad447

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RestartServerResponse response definition.
message RestartServerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### send_websocket_message_request.proto {#send_websocket_message_request}

**Path**: `gcommon/v1/web/send_websocket_message_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `SendWebsocketMessageRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/send_websocket_message_request.proto
// version: 1.0.0
// guid: 0f379368-5941-4e80-a7c6-3d66aafd5d54

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SendWebsocketMessageRequest request definition.
message SendWebsocketMessageRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### send_websocket_message_response.proto {#send_websocket_message_response}

**Path**: `gcommon/v1/web/send_websocket_message_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `SendWebsocketMessageResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/send_websocket_message_response.proto
// version: 1.0.0
// guid: 844cd4f0-f98b-4548-8b5a-fd4b1cc457ff

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SendWebsocketMessageResponse response definition.
message SendWebsocketMessageResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### serve_static_request.proto {#serve_static_request}

**Path**: `gcommon/v1/web/serve_static_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ServeStaticRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/serve_static_request.proto
// version: 1.0.0
// guid: ed014e20-4f0a-447b-8c14-ef6b0f967b36

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ServeStaticRequest request definition.
message ServeStaticRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### serve_static_response.proto {#serve_static_response}

**Path**: `gcommon/v1/web/serve_static_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ServeStaticResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/serve_static_response.proto
// version: 1.0.0
// guid: d3354a82-ddd1-48c8-956b-d715c8f9ac83

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ServeStaticResponse response definition.
message ServeStaticResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### start_server_request.proto {#start_server_request}

**Path**: `gcommon/v1/web/start_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Messages** (1): `StartServerRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/start_server_request.proto
// version: 1.0.1
// guid: 25892d63-79d6-4211-8d7e-aa4cdbf1fa99
// StartServerRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message StartServerRequest {
  // Server ID
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### start_server_response.proto {#start_server_response}

**Path**: `gcommon/v1/web/start_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `StartServerResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/server_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/start_server_response.proto
// version: 1.0.1
// guid: 0655b1fa-e5f9-419d-a4f1-dcd1a5b474b5

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/server_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StartServerResponse response definition.
message StartServerResponse {
  // Success status
  bool success = 1;

  // Server status
  gcommon.v1.common.ServerStatus status = 2;

  // Listen address
  string listen_address = 3 [(buf.validate.field).string.min_len = 1];

  // Error information
  gcommon.v1.common.Error error = 4;
}
```

---

### stop_server_request.proto {#stop_server_request}

**Path**: `gcommon/v1/web/stop_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `StopServerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/stop_server_request.proto
// version: 1.0.0
// guid: 400d2dd2-87fd-497d-99e3-a7c2470f7377

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StopServerRequest request definition.
message StopServerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_server_response.proto {#stop_server_response}

**Path**: `gcommon/v1/web/stop_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `StopServerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/stop_server_response.proto
// version: 1.0.0
// guid: 968f4a2e-5b03-4188-8c64-209017b813da

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StopServerResponse response definition.
message StopServerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_handler_request.proto {#unregister_handler_request}

**Path**: `gcommon/v1/web/unregister_handler_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterHandlerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_handler_request.proto
// version: 1.0.0
// guid: b3a2283a-da75-498d-bcd6-73068020f71f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterHandlerRequest request definition.
message UnregisterHandlerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_handler_response.proto {#unregister_handler_response}

**Path**: `gcommon/v1/web/unregister_handler_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterHandlerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_handler_response.proto
// version: 1.0.0
// guid: 60c00ce0-2fa0-4af1-a7ab-48b4351a72cf

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterHandlerResponse response definition.
message UnregisterHandlerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_middleware_request.proto {#unregister_middleware_request}

**Path**: `gcommon/v1/web/unregister_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Messages** (1): `UnregisterMiddlewareRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_middleware_request.proto
// version: 1.1.0
// guid: 9123fb9b-ced5-4251-adb0-dcb9b453b8b5
// UnregisterMiddlewareRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UnregisterMiddlewareRequest {
  // Server identifier
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Middleware identifier
  string middleware_id = 2 [(buf.validate.field).string.min_len = 1];

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### unregister_middleware_response.proto {#unregister_middleware_response}

**Path**: `gcommon/v1/web/unregister_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `UnregisterMiddlewareResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_middleware_response.proto
// version: 1.1.1
// guid: 008a5536-7226-40b2-8424-92dcc7075e14

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterMiddlewareResponse response definition.
message UnregisterMiddlewareResponse {
  // Operation success flag
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;
}
```

---

### unregister_route_request.proto {#unregister_route_request}

**Path**: `gcommon/v1/web/unregister_route_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterRouteRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_route_request.proto
// version: 1.0.0
// guid: 6bd8df0c-0003-4464-b76f-837bb1a72af6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterRouteRequest request definition.
message UnregisterRouteRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_route_response.proto {#unregister_route_response}

**Path**: `gcommon/v1/web/unregister_route_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterRouteResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_route_response.proto
// version: 1.0.0
// guid: 701eb2b6-d704-4e56-9ee0-ad1a1e244453

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterRouteResponse response definition.
message UnregisterRouteResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_cookie_request.proto {#update_cookie_request}

**Path**: `gcommon/v1/web/update_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCookieRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cookie_request.proto
// version: 1.0.0
// guid: 3762d335-0618-4954-be4c-297ba3a2ed8e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCookieRequest request definition.
message UpdateCookieRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_cookie_response.proto {#update_cookie_response}

**Path**: `gcommon/v1/web/update_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cookie_response.proto
// version: 1.0.0
// guid: e817a298-f3a9-4451-bdc6-e8967ed8175e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCookieResponse response definition.
message UpdateCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_session_request.proto {#update_session_request}

**Path**: `gcommon/v1/web/update_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `WebUpdateSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_session_request.proto
// version: 1.1.0
// guid: 4c543371-4882-4a5c-9fe2-481de3738e67

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSessionRequest request definition.
message WebUpdateSessionRequest {
  // Identifier of the session to update
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // New metadata to apply
  map<string, string> metadata = 2;
}
```

---

### update_session_response.proto {#update_session_response}

**Path**: `gcommon/v1/web/update_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebUpdateSessionResponse`

**Imports** (2):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_session_response.proto
// version: 1.1.1
// guid: f1b380a2-162b-44ad-a6c0-5fd39e3add91

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSessionResponse response definition.
message WebUpdateSessionResponse {
  // Updated session data
  SessionData session = 1;
}
```

---

### update_ssl_certificate_request.proto {#update_ssl_certificate_request}

**Path**: `gcommon/v1/web/update_ssl_certificate_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `UpdateSSLCertificateRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_ssl_certificate_request.proto
// version: 1.0.1
// guid: eec70ef5-baf4-4799-ba2d-3b00ad4b2e32

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * UpdateSSLCertificateRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message UpdateSSLCertificateRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

### update_ssl_certificate_response.proto {#update_ssl_certificate_response}

**Path**: `gcommon/v1/web/update_ssl_certificate_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `UpdateSSLCertificateResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_ssl_certificate_response.proto
// version: 1.0.1
// guid: f2ee4b98-5830-4ea9-a968-5cf5c6216d5d

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * UpdateSSLCertificateResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message UpdateSSLCertificateResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}
```

---

### upload_file_request.proto {#upload_file_request}

**Path**: `gcommon/v1/web/upload_file_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UploadFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/upload_file_request.proto
// version: 1.0.0
// guid: c341b4e3-de76-449b-93d0-fbb1fe4e1655

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UploadFileRequest request definition.
message UploadFileRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### upload_file_response.proto {#upload_file_response}

**Path**: `gcommon/v1/web/upload_file_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UploadFileResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/upload_file_response.proto
// version: 1.0.0
// guid: d6f9dad0-3449-4808-b710-f73253ba1b06

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UploadFileResponse response definition.
message UploadFileResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### validate_csrf_token_request.proto {#validate_csrf_token_request}

**Path**: `gcommon/v1/web/validate_csrf_token_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ValidateCsrfTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/validate_csrf_token_request.proto
// version: 1.0.0
// guid: a28f712d-4b1c-417b-ad6c-eb154c429933

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ValidateCsrfTokenRequest request definition.
message ValidateCsrfTokenRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### validate_csrf_token_response.proto {#validate_csrf_token_response}

**Path**: `gcommon/v1/web/validate_csrf_token_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ValidateCsrfTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/validate_csrf_token_response.proto
// version: 1.0.0
// guid: d29634a2-4e04-442d-9de5-e11d1e300ed4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ValidateCsrfTokenResponse response definition.
message ValidateCsrfTokenResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### server_event.proto {#server_event}

**Path**: `gcommon/v1/web/server_event.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ServerEvent`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_event.proto
// version: 1.2.0
// guid: 2b778529-ccd9-45f1-bf97-9f4ebfa8b1e9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

// Standard imports

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * ServerEvent represents events generated by web servers.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ServerEvent {
  // Required fields (1-10)

  /**
   * Type of server event.
   */
  string event_type = 1 [(buf.validate.field).string.min_len = 1];

  /**
   * Event data payload.
   */
  google.protobuf.Any event_data = 2;

  // Optional fields (11-50)

  /**
   * Server ID that generated this event.
   */
  string server_id = 11 [(buf.validate.field).string.min_len = 1];

  /**
   * Additional event metadata.
   */
  string metadata = 12;

  // Timestamps (51-60)

  /**
   * Timestamp when this event occurred.
   */
  google.protobuf.Timestamp event_time = 51;
}
```

---

### stream_server_events_request.proto {#stream_server_events_request}

**Path**: `gcommon/v1/web/stream_server_events_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `StreamServerEventsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/stream_server_events_request.proto
// version: 1.0.1
// guid: 0316e0ad-e7e2-4a26-82d6-0a4b3d92c9ec

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * StreamServerEventsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message StreamServerEventsRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}
```

---

