import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="Click Me",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual(node.to_html(), "<p>Hello world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me</a>')
