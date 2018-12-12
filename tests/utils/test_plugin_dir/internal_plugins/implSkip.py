"""
Example of a module that implements implementations but states that nothing is
exported by setting the helper variable to ``None``.
"""
from tests.utils.test_plugin_dir.internal_plugins.interface import \
    DummyInterface


class ImplSkipModule (DummyInterface):

    @classmethod
    def is_usable(cls):
        return True

    def inst_method(self, val):
        return "skipModule"+str(val)


TEST_PLUGIN_CLASS = None
