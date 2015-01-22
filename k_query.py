"""k_query

This is a module aimed at extending Kivy with some extra definitions and
methods which allows for a more dynamic UI. As the name implies, it is meant
to somewhat resemble JavaScript's jQuery.

If you're just trying to get started with this, load your data structure (I
would recommend building from a .kv file) and use the following line:

KQuery.setup(root) # Or whatever the root node is for your interface
"""
import re


class KQuery:
    """KQuery class

    This is the constructor for KQuery objects, which individually have their
    own methods for appending, deleting, and traversing the document tree.
    """
    @classmethod
    def setup(cls, root, debug):
        """Sets up the KQuery class for use in an application"""
        cls.root = root
        cls.debug = debug

    def __init__(self, arg1, arg2=""):
        """This is a polymorphic function. The first argument is required,
        and the second is optional.

        If the first argument is a selector (string), then a set of results
        will be constructed using a search on the selector.

        If the first argument is an object instance, the KQuery object will
        be constructed by adding the selector.
        """
        # Must ensure that root is defined for this module
        try:
            self.root
        except:
            raise RootNotDefined("Root widget was not defined! Please refer \
                to the documentation [help(k_query)].")

        if type(arg1) is str:
            # If arg1 is a selector, we are searching for a widget
            self.selector = arg1
            self.widgets = _search(selector=arg1)
        else:
            # If arg1 is a KQuery instance, we are constructing an object
            self.selector = arg2
            self.widgets = set(arg1)

    def __str__(self):
        return "KQuery object with selector " + self.selector

    def _search(self, selector=None, ids=None, classes=None):
        """Uses a BFS algorithm to look for elements matching a selector"""
        if selector is not None:
            items = _split_selector(selector)
            _search(ids=items[0], classes=items[1])


    def _split_selector(self, selector):
        ids = re.findall("#[a-zA-Z]+", selector)
        classes = re.findall("\.[a-zA-Z]+", selector)
        return (ids, classes)

    def append(self, other):
        """Appends a KQuery object to this widget"""
        pass

    def append_to(self, other):
        """Appends this KQuery object to a widget"""
        pass

    def bind(self):
        """Bind a function to an event handler.

        Add a parameter to allow binding to future widgets?"""
        pass

    def children(self):
        """Return list of children of this widget"""
        pass

    def closest(self):
        """Return nearest instance of selector parameter from this widget"""
        pass

    def data(self, attribute, value=None):
        """Assigns a value to an object attribute"""
        pass

    def each(self):
        """Apply function parameter to all instances of a KQuery object"""
        pass

    def empty(self):
        """Clears all children from a widget"""
        self.clear_widgets()

    def eq(self):
        """Filter KQuery results to one at provided index"""
        pass

    def height(self):
        """Get height of an widget"""
        pass

    def parent(self):
        """Get parent of an widget"""
        pass

    def prepend(self):
        """Prepend parameter to this widget"""
        pass

    def prepend_to(self):
        """Prepend this widget to the parameter"""
        pass

    def remove(self):
        """Remove this widget from the widget tree"""
        pass

    def text(self):
        """Return the text of the widget if available, or reassign it if the
        corresponding parameter is given.
        """
        pass

    def unbind(self):
        """Unbind an event handler from the set of matched widgets."""
        pass

    def width(self):
        """Return the width of a widget"""
        pass