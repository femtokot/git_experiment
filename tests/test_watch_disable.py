import py.test
import watch


def test_toggle_scenario_for_types():

    class A(watch.WatchMe):
        foo = watch.builtins.InstanceOf(int)

    class B(watch.WatchMe):
        foo = watch.builtins.InstanceOf(int)

    a = A()
    b = B()

    # default scenario for a
    with py.test.raises(AttributeError):
        a.foo = "hello"

    # default scenario for b
    with py.test.raises(AttributeError):
        b.foo = "hello"

    A.keep_eye_on_me = False
    a.foo = "hello"
    assert a.foo == "hello"

    # disabling watch for A has nothing to do with B
    with py.test.raises(AttributeError):
        b.foo = "hello"

    # now watch is disabled globaly
    watch.WatchMe.keep_eye_on_me = False

    a.foo = "hello"
    assert a.foo == "hello"

    b.foo = "hello"
    assert b.foo == "hello"

    watch.WatchMe.keep_eye_on_me = True


def test_toggle_scenario_for_instances():

    class A(watch.WatchMe):
        foo = watch.builtins.InstanceOf(int)

    a = A()
    b = A()

    a.keep_eye_on_me = False
    a.foo = "hello"
    assert a.foo == "hello"

    # default scenario for b
    with py.test.raises(AttributeError):
        b.foo = "hello"

    watch.WatchMe.keep_eye_on_me = True

