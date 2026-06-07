# Certificate Verification Notes

The certificate generator creates signed verification data for attendance certificates. The private signing key stays off GitHub.

## Public Pieces

These files can stay public:

- generator source code
- fake sample attendee input
- certificate template assets
- public verification key
- documentation for the verification flow

## Private Pieces

Do not commit:

- `.certificate_keys/private_key.pem`
- real attendee files
- generated certificates
- generated manifests
- screenshots that expose attendee emails or private QR payloads

## Expected Verification Flow

1. The generator signs certificate metadata with the private key.
2. The certificate QR code points to the verification website.
3. The verification website checks the signed token with the public key.
4. The website shows whether the certificate is valid.

The verifier does not need the private key. If the verifier asks for a private key, stop and review the implementation.

## Public Key Rotation

When maintainers rotate the signing key:

- keep old public keys available for old certificates
- use the new private key only for new certificates
- document the key version used for each certificate batch
- keep the old verification URL redirected if old QR codes point to it

## Suggested Verifier Repository Shape

If the team adds the verifier to this repo later, use a separate folder:

```text
tools/certificate-verifier/
```

Keep verifier deployment settings public-safe. Use environment variables for deployment-only values.

