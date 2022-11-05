import hello;

# Example Passing Test
def test_hello_pass():
    assert hello.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert hello.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# Problem 1 Tests
def test_squared_sum_empty():
    assert hello.squared_sum( [] ) == 0

def test_squared_sum1():
    assert hello.squared_sum([4]) == 16

def test_squared_sum2():
    assert hello.squared_sum([-3, 4]) == 25

def test_squared_sum3():
    assert hello.squared_sum([5, -2, 3]) == 38

def test_squared_sum4():
    assert hello.squared_sum([7, -1, 15, 0]) == 275

# Problem 2 Tests
def test_mix_empty():
    assert hello.mix("", "") == ""

def test_mix_even():
    assert hello.mix("hello", "there") == "htehlelroe"

def test_mix_4_4():
    assert hello.mix("1234", "abcd") == "1a2b3c4d"

def test_mix_2_4():
    assert hello.mix("12", "abcd") == "1a2bcd"

def test_mix_4_2():
    assert hello.mix("1234", "ab") == "1a2b34"