from unittest import TestCase
from secret import run_jwt_decode, get_parameter


class Test(TestCase):
    def test_run_jwt_decode(self):
        decode = run_jwt_decode()
        print(decode)
        self.assertTrue(decode == 1)

#
# class Test(TestCase):
#     def test_get_parameter(self):
#         secret = get_parameter(f"/1/runtime/snd/max_jwt_key", True)
#         self.aasertTrue(secret == 69)
