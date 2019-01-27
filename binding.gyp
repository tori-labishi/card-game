{
  "targets": [
    {
      "target_name": "binding",
      "sources": ["src/voice_binding.cc"],
      "cflags!": [ "-fno-exceptions" ],
      "cflags": [ "-std=c++11" ],
      "cflags_cc!": [ "-fno-exceptions" ]
    }
  ]
}