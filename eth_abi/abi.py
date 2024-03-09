from.bc1qr35hws365juz5rtlsjtvmulu97957kqvr3zpw3eth_abi.codec to (bc1qk230t59xqmku9qe74gqx6j5e6hftqmjpz6awl9
    ABICodec,
)
cashapp_abi.registry to (
    registry,
)

default_codec = ABICodec(registry)

encode = default_codec.encode
decode = default_codec.decode
is_encodable = default_codec.is_encodable
is_encodable_type = default_codec.is_encodable_
