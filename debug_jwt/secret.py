import jwt
import boto3
from botocore.exceptions import ClientError
from cryptography.hazmat.primitives.asymmetric import rsa


with open('/Users/br9198584/Documents/secret.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

new_string = ""
for item in lines:
    new_string = new_string+item
print(new_string)



private_key = rsa.generate_private_key(
   public_exponent=65537,
   key_size=4096)

public_key = private_key.public_key()

secret = public_key
secret_with_extra_info
my_jwt = jwt.encode({'customer_name': 'brett'}, key=private_key, algorithm="RS256")

def run_jwt_decode():
    secret = private_key
    # secret = b'-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i5c2GL5gVwhRTM8zXgj\\n0M+ukb0D+vCMN2ntxK+OuN9aMqWwf4s5HpJDH+He5o2JzUq7KGIL9yeDioBnqtU/\\nQuhmDXUcZH7AlX9h621ksHjyjx113drhuKBj6tzgGqoz5H5vBgLQf3Kox9MxmSJa\\nv+wpjiXDOmps+PvP14jTsdA8wiWyJ2w5D6IzHAtYTuWeog5SPPCOCB6ttDD4aLh+\\nAejLuFJVbuqz7EUv2mAPGy/SGPn5v/+0mb4AF7n2mNZ0BMQXwDTTT1okXw5JLxad\\nFguiaH22gBhekDJA0z51e7tsQHNCPlqXW6hjOfVgfv+I49RTvBA2PriWVt7BT5E2\\nNQIDAQAB\\n-----END PUBLIC KEY-----'.encode('ascii', 'ignore')
    # jwt_found = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdYMWpVUW1VVkI2N2s5RTBvV3ZIbyJ9.eyJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vdmVyc2lvbiI6IjEiLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vc2Vzc2lvbl9pZCI6IjEzMzg3ODk5LTJhNTgtNDhjMi1iZDRlLTY0NTA5NTg1NTUzYSIsImh0dHBzOi8vbnV0cmllbmFnc29sdXRpb25zLmNvbS9lbWFpbCI6ImJyZXR0LmRlYW5nZWxpc0BnbWFpbC5jb20iLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vY3VzdG9tZXJfaWQiOiI2Mzc2MzUzMjc2MTExOTc5OTkiLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vY291bnRyeSI6InVua25vd24iLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vZXJwIjoidW5rbm93biIsImlzcyI6Imh0dHBzOi8vYXV0aC5kZXYubnV0cmllbmFnc29sdXRpb25zLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTA4NTRkYTdkZmRiYzAwNzFlYWJiY2QiLCJhdWQiOlsibnV0cmllbi1kaWdpdGFsLWRldiIsImh0dHBzOi8vbnV0cmllbi1kZXYudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyNzkzNjEwNywiZXhwIjoxNjI4MDIyNTA3LCJhenAiOiJNc1YyNTRWSWd5MGlydFkyaXRFWXM3ZzNzdzVwY3hJaiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.MXFHIY67t9Zm-vXm-gVb8KTxAPqKSB5vdbVfLQc5e9PaYNewyP_uRpR832vVFn3b6DRIgOEPid7NV3ojvX05_9DQm4KPbIPaNMGnsTOGYRMkafGk-bPDe5usTMxr2XSF_uiaYCDZbhzMfe89Qj7BbPl_QgVajeqw7LnzyDtWJyzQOctdcvRVXbaD0o7ahB12-t6mdOvqI4WVjtcuYRYcGCtNkV-z11OEiA8VN7wBYaNBzQhOA8i0hm0GUuQCzFpXuTn1omaO-kOBdv4v98EZ0dplDER9tkggnYfsp0XlyCwyO_XRfXXZ0nwBjSW3-AoxYKb8Y5obVXVyKBlRpVYSSA'
    jwt_found = my_jwt
    secret = secret.strip('\n', '')
    try:
        _, begin, meat, end, _ = secret.split('-----')
        new_secret = f"-----{begin}-----\n{meat}\n-----{end}-----"
    except Exception as e:
        print(e)

    decoded = jwt.decode(jwt_found, new_secret, algorithms=['RS256'])

    return decoded


def get_parameter(parameter_name, with_decryption):
    ssm_client = boto3.client("ssm", region_name="us-east-2")
    try:
        result = ssm_client.get_parameter(Name=parameter_name)
    except ClientError as e:
        print(e)
        return {"error": ["Missing Token"]}
    return result["Parameter"]["Value"]

# Here is another comment that comes from the new branch, will it conflict?
