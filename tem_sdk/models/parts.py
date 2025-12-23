from pydantic import AliasChoices, BaseModel, Field


class SignedMS(BaseModel):
    """
    SignedMS model used to represent a multisignature payload for authorizing requests.

    Fields:
        message (str): A message identifier that must match the pattern.
            Typically this is a compact identifier produced by the signing process and
            prefixed with `te_`. Example: `"te_abc123"`.
        signature (str): The cryptographic signature corresponding to `message`.
            This should be the signature string produced by the signing key and is used
            by the server to verify the authenticity of the request.

    Notes:
        - This model inherits from `pydantic.BaseModel` and performs validation on the
          `message` field using the provided regex pattern.
        - Do not include internal/private fields used by the signing implementation in
          external requests.
    """

    message: str = Field(
        ...,
        pattern=r"^te_\w+$",
        validation_alias=AliasChoices(
            "message",
            "Message",
        ),
    )
    signature: str = Field(
        ...,
        validation_alias=AliasChoices(
            "signature",
            "Signature",
        ),
    )
