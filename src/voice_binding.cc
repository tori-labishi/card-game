#include <iostream>
#include <node_api.h>

napi_value VoicePlugin(
  napi_env env,
  napi_value exports
) {
  std::cout << "setup voice plugin" << std::endl;
  return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, VoicePlugin);