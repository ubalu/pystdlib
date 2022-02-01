import pystdlib as std

def test_iota():
	i = std.Iota()
	assert i.iota() == 0
	assert i.iota_counter == 1

	assert i.iota() == 1
	assert i.iota_counter == 2

	i.reset()
	assert i.iota_counter == 0


def test_hcf():
	print("[test_pystdlib.py::test_hcf()] Test this on your own, alright?")
	# print("[test_pystdlib.py::test_hcf()] If you text after this one, the test has failed")
	# std.hcf(die = True)
	# assert False, "[test_pystdlib.py::test_hcf()] Well, this had failed, didn't it?"
test_iota()
test_hcf()