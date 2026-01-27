import { EncodeDecode } from "./encode-decode";

test("EncodeDecode basic", () => {
    const codec = new EncodeDecode();
    const input = ["neet", "code", "love", "you"];
    const encoded = codec.encode(input);
    const decoded = codec.decode(encoded);
    expect(decoded).toEqual(input);
});

test("EncodeDecode with symbols", () => {
    const codec = new EncodeDecode();
    const input = ["ne#et", "code", "love", "#you"];
    const encoded = codec.encode(input);
    const decoded = codec.decode(encoded);
    expect(decoded).toEqual(input);
});

test("EncodeDecode empty", () => {
    const codec = new EncodeDecode();
    const input = [""];
    const encoded = codec.encode(input);
    const decoded = codec.decode(encoded);
    expect(decoded).toEqual(input);
});
