import jwt
import boto3
from botocore.exceptions import ClientError


with open('/Users/br9198584/Documents/secret.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

new_string = ""
for item in lines:
    new_string = new_string+item
print(new_string)


def run_jwt_decode():
    secret = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i5c2GL5gVwhRTM8zXgj\n0M+ukb0D+vCMN2ntxK+OuN9aMqWwf4s5HpJDH+He5o2JzUq7KGIL9yeDioBnqtU/\nQuhmDXUcZH7AlX9h621ksHjyjx113drhuKBj6tzgGqoz5H5vBgLQf3Kox9MxmSJa\nv+wpjiXDOmps+PvP14jTsdA8wiWyJ2w5D6IzHAtYTuWeog5SPPCOCB6ttDD4aLh+\nAejLuFJVbuqz7EUv2mAPGy/SGPn5v/+0mb4AF7n2mNZ0BMQXwDTTT1okXw5JLxad\nFguiaH22gBhekDJA0z51e7tsQHNCPlqXW6hjOfVgfv+I49RTvBA2PriWVt7BT5E2\nNQIDAQAB\n-----END PUBLIC KEY-----'
    # secret = b'-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i5c2GL5gVwhRTM8zXgj\\n0M+ukb0D+vCMN2ntxK+OuN9aMqWwf4s5HpJDH+He5o2JzUq7KGIL9yeDioBnqtU/\\nQuhmDXUcZH7AlX9h621ksHjyjx113drhuKBj6tzgGqoz5H5vBgLQf3Kox9MxmSJa\\nv+wpjiXDOmps+PvP14jTsdA8wiWyJ2w5D6IzHAtYTuWeog5SPPCOCB6ttDD4aLh+\\nAejLuFJVbuqz7EUv2mAPGy/SGPn5v/+0mb4AF7n2mNZ0BMQXwDTTT1okXw5JLxad\\nFguiaH22gBhekDJA0z51e7tsQHNCPlqXW6hjOfVgfv+I49RTvBA2PriWVt7BT5E2\\nNQIDAQAB\\n-----END PUBLIC KEY-----'.encode('ascii', 'ignore')
    # jwt_found = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdYMWpVUW1VVkI2N2s5RTBvV3ZIbyJ9.eyJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vdmVyc2lvbiI6IjEiLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vc2Vzc2lvbl9pZCI6IjEzMzg3ODk5LTJhNTgtNDhjMi1iZDRlLTY0NTA5NTg1NTUzYSIsImh0dHBzOi8vbnV0cmllbmFnc29sdXRpb25zLmNvbS9lbWFpbCI6ImJyZXR0LmRlYW5nZWxpc0BnbWFpbC5jb20iLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vY3VzdG9tZXJfaWQiOiI2Mzc2MzUzMjc2MTExOTc5OTkiLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vY291bnRyeSI6InVua25vd24iLCJodHRwczovL251dHJpZW5hZ3NvbHV0aW9ucy5jb20vZXJwIjoidW5rbm93biIsImlzcyI6Imh0dHBzOi8vYXV0aC5kZXYubnV0cmllbmFnc29sdXRpb25zLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTA4NTRkYTdkZmRiYzAwNzFlYWJiY2QiLCJhdWQiOlsibnV0cmllbi1kaWdpdGFsLWRldiIsImh0dHBzOi8vbnV0cmllbi1kZXYudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyNzkzNjEwNywiZXhwIjoxNjI4MDIyNTA3LCJhenAiOiJNc1YyNTRWSWd5MGlydFkyaXRFWXM3ZzNzdzVwY3hJaiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.MXFHIY67t9Zm-vXm-gVb8KTxAPqKSB5vdbVfLQc5e9PaYNewyP_uRpR832vVFn3b6DRIgOEPid7NV3ojvX05_9DQm4KPbIPaNMGnsTOGYRMkafGk-bPDe5usTMxr2XSF_uiaYCDZbhzMfe89Qj7BbPl_QgVajeqw7LnzyDtWJyzQOctdcvRVXbaD0o7ahB12-t6mdOvqI4WVjtcuYRYcGCtNkV-z11OEiA8VN7wBYaNBzQhOA8i0hm0GUuQCzFpXuTn1omaO-kOBdv4v98EZ0dplDER9tkggnYfsp0XlyCwyO_XRfXXZ0nwBjSW3-AoxYKb8Y5obVXVyKBlRpVYSSA'
    jwt_found = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2ZWU3NzNmYi04MTQwLTQ1Y2YtOThiNi05M2ZlZjFkOGNiMTgiLCJ1c2VybmFtZSI6ImJyZXR0LmRlYW5nZWxpc0BudXRyaWVuLmNvbSIsInByb3ZpZGVyIjoiYWRmcyIsImlzcyI6Imh0dHBzOi8vY29yZS1zZXJ2aWNlcy1hdXRoLmRldi5jcHMtY29yZS5jb20iLCJzdWIiOiJicmV0dC5kZWFuZ2VsaXNAbnV0cmllbi5jb20iLCJuYmYiOjE2MjgwMDI4NTgsImlhdCI6MTYyODAwMjg1OCwiZXhwIjoxNjI4MDM4ODU4LCJhdHRyaWJ1dGVzIjp7InNlc3Npb25JZCI6ImI5ZGZlYzRmMTdmYjliMDYzNGU2NDE4OTI4ODdjNWIxIiwiYWRmc1VzZXJuYW1lIjoiYnI5MTk4NTg0Iiwic3VwcG9ydCI6ZmFsc2UsImVtYWlsIjoiYnJldHQuZGVhbmdlbGlzQG51dHJpZW4uY29tIn19.lFgg1l8gSsfhjJEzvJBkZXyjqznflNgt6nhcEQP-Kdv2yy46cd0QJcumwEgGD851nDW5jsQQPTYShA6itZItRgtzR5UXD7AKrY-E2Xs0wp6Tdw2MMaebq3B1IpF5Jx8uAeaI0UhU5yMVvJZfNY-nOziphC3FMoEIEWXGIXKBn0wzC9op4izVfXEdrEkUvfenP4s_9CigsDP7Oj7ZyZ3vfIXMMzdkhLwEETO5urHFWX-xQh9rFWRZ7POZ5RylcOzo_8VvflUcFDub8zu0T3VhGW0MjQLxFYpGjYJ5_F_Byb64Te95df_BSu7epCvWolL_vOorSrWXuwsedjp0XpxKOA'
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

# Making this change on the main branch will it stay or cause a conflict
