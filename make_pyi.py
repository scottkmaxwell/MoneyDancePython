# !/usr/bin/env python
# coding=utf-8
# Python script to inspect the MoneyDance Python API

# TODO: Handle overloaded methods

from __future__ import print_function

try:
    # noinspection PyUnresolvedReferences
    from typing import Dict, Generator, Iterator, List, Optional, Set, Tuple, Union, Any, TYPE_CHECKING
    if TYPE_CHECKING:
        unicode = str
except ImportError:
    pass

import importlib
import inspect
import os.path
import re

class MethodDetails:
    def __init__(self, result=None, params=''):
        self.result = result
        self.params = params


class_info = {
    'com.infinitekind.moneydance.model.Account': {
        'adjustStartBalance': MethodDetails(params='adjust_amount: int'),
    },
    'javax.print.attribute.standard.JobName': {
        '__init__': MethodDetails(params='s: str, j: typing.Optional[java.util.Locale]'),
    },
}

class_extra_lines = {
    'com.moneydance.awt.JTextPanel': [
        "def __init__(self, title: str) -> None: ...",
    ],
    'java.awt.Color': [
        "@typing.overload",
        "def __init__(self, r: int, g: int, b: int, a: int = 0) -> None: ...",
    ],
    'java.awt.Component': [
        "def getFont(self) -> 'java.awt.Font': ...",
    ],
    'java.awt.Container': [
        "def removeAll(self) -> None: ...",
        "def add(self, comp: 'Component', index: int = 0) -> 'Component': ...",
        "@typing.overload",
        "def add(self, name: str, comp: 'Component') -> 'Component': ...",
    ],
    'java.awt.Dialog': [
        "def setVisible(self, b: bool) -> None: ...",
    ],
    'java.awt.Dimension': [
        "@typing.overload",
        "def __init__(self, width: int, height: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, d: 'Dimension') -> None: ...",
    ],
    'java.awt.FileDialog': [
        "LOAD: int",
        "SAVE: int",
        "def __init__(self, parent: Dialog, title: str = "", mode: int = 0) -> None: ...",
        "@typing.overload",
        "def __init__(self, parent: Frame, title: str = "", mode: int = 0) -> None: ...",
        "def getDirectory(self) -> str: ...",
        "def getFile(self) -> str: ...",
        "def setDirectory(self, dir: str) -> None: ...",
        "def setFile(self, file: str) -> None: ...",
        "def setFilenameFilter(self, filename_filter: java.io.FilenameFilter) -> None: ...",
        "def setMode(self, mode: int) -> None: ...",
        "def setMultipleMode(self, enabled: bool) -> None: ...",
        "def setTitle(self, title: str) -> None: ...",
    ],
    'java.awt.Font': [
        "@typing.overload",
        "def deriveFont(self, size: float) -> 'Font': ...",
        "@typing.overload",
        "def __init__(self, font: 'Font') -> None: ...",
        "@typing.overload",
        "def __init__(self, name: str, style: int, size: int) -> None: ...",
    ],
    'java.awt.FlowLayout': [
        "@typing.overload",
        "def __init__(self, align: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, align: int, hgap: int, vgap: int) -> None: ...",
    ],
    'java.awt.print.PrinterJob': [
        "@typing.overload",
        "def printDialog(self, attributes: javax.print.attribute.PrintRequestAttributeSet) -> bool: ...",
        "@typing.overload",
        "def setPrintable(self, printable: 'Printable', format: PageFormat) -> None: ...",
    ],
    'java.awt.Window': [
        "def dispose(self) -> None: ...",
    ],
    'java.lang.System': [
        "@typing.overload",
        "@staticmethod",
        "def getProperty(key: str, default: str) -> str: ...",
    ],
    'javax.print.attribute.HashPrintRequestAttributeSet': [
        "@typing.overload",
        "def __init__(self, o: PrintRequestAttributeSet) -> None: ...",
    ],
    'javax.swing.border.EmptyBorder': [
        "@typing.overload",
        "def __init__(self, top: int, left: int, bottom: int, right: int) -> None: ...",
    ],
    'javax.swing.Box': [
        "def createRigidArea(d: java.awt.Dimension) -> java.awt.Component: ...",
    ],
    'javax.swing.JButton': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, icon: 'Icon') -> None: ...",
        "@typing.overload",
        "def __init__(self, action: 'Action') -> None: ...",
        "@typing.overload",
        "def __init__(self, icon: 'Icon') -> None: ...",
    ],
    'javax.swing.JCheckBox': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, selected: bool) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, icon: 'Icon') -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, icon: 'Icon', selected: bool) -> None: ...",
        "@typing.overload",
        "def __init__(self, action: 'Action') -> None: ...",
        "@typing.overload",
        "def __init__(self, icon: 'Icon') -> None: ...",
        "@typing.overload",
        "def __init__(self, icon: 'Icon', selected: bool) -> None: ...",
    ],
    'javax.swing.JComponent': [
        "TOOL_TIP_TEXT_KEY: str",
        "UNDEFINED_CONDITION: int",
        "WHEN_ANCESTOR_OF_FOCUSED_COMPONENT: int",
        "WHEN_FOCUSED: int",
        "WHEN_IN_FOCUSED_WINDOW: int",
        "def getClientProperty(self, key: Any) -> Any: ...",
        "def putClientProperty(self, key: Any, value: Any) -> None: ...",
        "def getFontMetrics(self) -> java.awt.FontMetrics: ..."
    ],
    'javax.swing.JDialog': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, owner: java.awt.Dialog, modal: bool) -> None: ...",
        "@typing.overload",
        "def __init__(self, owner: java.awt.Dialog, title: str = "", modal: bool = False, gc: typing.Optional[java.awt.GraphicsConfiguration] = None) -> None: ...",
        "@typing.overload",
        "def __init__(self, owner: java.awt.Frame, modal: bool) -> None: ...",
        "@typing.overload",
        "def __init__(self, owner: java.awt.Frame, title: str = "", modal: bool = False, gc: typing.Optional[java.awt.GraphicsConfiguration] = None) -> None: ...",
        "@typing.overload",
        "def __init__(self, owner: java.awt.Window, modality: java.awt.Dialog.ModalityType) -> None: ...",
        "@typing.overload",
        "def __init__(self, owner: java.awt.Window, title: str = "", modality: java.awt.Dialog.ModalityType = java.awt.Dialog.ModalityType.MODELESS, gc: typing.Optional[java.awt.GraphicsConfiguration] = None) -> None: ...",
    ],
    'javax.swing.JFileChooser': [
        "APPROVE_OPTION: int",
        "CANCEL_OPTION: int",
        "ERROR_OPTION: int",
        "DIRECTORIES_ONLY: int",
        "FILES_ONLY: int",
        "FILES_AND_DIRECTORIES: int",
        "def __init__(self, title: str = '') -> None: ...",
        "def getSelectedFile(self) -> java.io.File: ...",
        "def setDialogTitle(self, title: str) -> None: ...",
        "def setFileFilter(self, file_filter: 'FileFilter') -> None: ...",
        "def setFileSelectionMode(self, mode: int) -> None: ...",
        "def setMultiSelectionEnabled(self, enabled: bool) -> None: ...",
        "def setSelectedFile(self, file: java.io.File): ...",
        "def showDialog(self, parent: java.awt.Component, approveButtonText: str) -> int: ...",
        "def showOpenDialog(self, parent: java.awt.Component) -> int: ...",
        "def showSaveDialog(self, parent: java.awt.Component) -> int: ...",
    ],
    'javax.swing.JFrame': [
        "def __init__(self, title: str) -> None: ...",
        "def getJMenuBar(self) -> 'JMenuBar': ...",
        "def setJMenuBar(self, menu_bar: 'Optional[JMenuBar]') -> None: ...",
    ],
    'javax.swing.JLabel': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, horizontalAlignment: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, icon: Icon, horizontalAlignment: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, icon: Icon) -> None: ...",
        "@typing.overload",
        "def __init__(self, icon: Icon, horizontalAlignment: int) -> None: ...",
    ],
    'javax.swing.JMenuBar': [
        "def add(self, menu: 'JMenu') -> 'JMenu': ...",
    ],
    'javax.swing.JOptionPane': [
        "INFORMATION_MESSAGE: int",
        "PLAIN_MESSAGE: int",
        "QUESTION_MESSAGE: int",
        "def showMessageDialog(parent_component: 'javax.swing.Component', message: Any, title: str = '', messageType: int = 0, icon: 'Optional[Icon]' = None) -> None: ...",
    ],
    'javax.swing.JPanel': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, isDoubleBuffered: bool) -> None: ...",
        "@typing.overload",
        "def __init__(self, layout_manager: java.awt.LayoutManager) -> None: ...",
        "@typing.overload",
        "def __init__(self, layout_manager: java.awt.LayoutManager, isDoubleBuffered: bool) -> None: ...",
    ],
    'javax.swing.JScrollPane': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, vsbPolicy: int, hsbPolicy: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, view: java.awt.Component) -> None: ...",
        "@typing.overload",
        "def __init__(self, view: java.awt.Component, vsbPolicy: int, hsbPolicy: int) -> None: ...",
    ],
    'javax.swing.JTextArea': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, rows: int, columns: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, rows: int, columns: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, doc: 'text.Document') -> None: ...",
        "@typing.overload",
        "def __init__(self, doc: 'text.Document', text: str, rows: int, columns: int) -> None: ...",
    ],
    'javax.swing.text.JTextComponent': [
        "def getText(self) -> str: ...",
    ],
    'javax.swing.JTextField': [
        "def __init__(self) -> None: ...",
        "@typing.overload",
        "def __init__(self, columns: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str) -> None: ...",
        "@typing.overload",
        "def __init__(self, text: str, columns: int) -> None: ...",
        "@typing.overload",
        "def __init__(self, doc: 'text.Document', text: str, columns: int) -> None: ...",
    ],
    'javax.swing.KeyStroke': [
        "def getText(self) -> str: ...",
        "@typing.overload",
        "@staticmethod",
        "def getKeyStoke(key: str, onKeyRelease: bool) -> 'KeyStroke': ...",
        "@typing.overload",
        "@staticmethod",
        "def getKeyStoke(key: str, modifiers: int) -> 'KeyStroke': ...",
        "@typing.overload",
        "@staticmethod",
        "def getKeyStoke(key_code: int, modifiers: int, onKeyRelease: bool = False) -> 'KeyStroke': ...",
    ],
}


typing = {'Callable', 'Dict', 'Iterator', 'Iterable', 'List', 'Mapping', 'Set', 'Sequence'}

starter_modules = {  # type: Set[str]
    "com.dropbox.core.v2",
    "com.google.gson",
    "com.infinitekind",
    "com.infinitekind.moneydance.model.txtimport",
    "com.moneydance",
    "com.moneydance.awt.graph",
    "com.moneydance.awt.ticker",
    "com.moneydance.awt.treetable",
    "java.awt",
    "java.io",
    "java.lang",
    "java.net",
    "java.security",
    "java.text",
    "java.util",
    "javax.print",
    "javax.swing",
    "org.antlr.runtime",
    "org.netbeans.swing",
    "org.xml.sax",
}
starter_modules_regex = re.compile("^(" + "|".join(starter_modules) + ")")
mem_ref_regex = re.compile("@[0-9a-f]{1,8}$")

specific_imports_to_ensure = """
from java.util import Locale
from java.lang import System, Runnable, IllegalArgumentException, String, Integer
from java.awt import Color, Dimension, Toolkit, Font, FileDialog, FlowLayout, BorderLayout
from java.awt.datatransfer import StringSelection
# from java.awt.event import KeyEvent, WindowAdapter
from java.awt import Point
from java.text import MessageFormat
from java.io import FilenameFilter, File

from javax.swing import SwingUtilities, JFrame, JOptionPane, JFileChooser, JDialog
from javax.swing import JButton, JScrollPane, WindowConstants, JComponent, KeyStroke, JLabel
from javax.swing import JTextArea, JMenuBar, AbstractAction
from javax.swing import Box, JCheckBox, JTextField, JPanel
from javax.swing.text import DefaultHighlighter
from javax.swing.event import AncestorListener
from javax.swing.border import EmptyBorder
from javax.swing.filechooser import FileFilter
from javax.print import attribute
from java.awt.print import PrinterJob

# java.awt.event.ActionListener
# java.awt.event.ComponentEvent
# java.awt.event.ActionEvent
# java.awt.event.FocusEvent
# java.awt.event.FocusListener
# java.awt.event.InputEvent
java.awt.Frame
java.awt.color.ColorSpace
java.awt.dnd.DropTarget
java.awt.dnd.DropTargetDragEvent
java.awt.dnd.DropTargetDropEvent
java.awt.dnd.DropTargetEvent
java.awt.dnd.DropTargetListener
java.awt.font.FontRenderContext
java.awt.font.GlyphVector
java.awt.font.LineMetrics
java.awt.font.TextAttribute
java.awt.geom.AffineTransform
java.awt.geom.Dimension2D
java.awt.geom.Point2D
java.awt.geom.Rectangle2D
java.awt.image.BufferedImage
java.awt.image.ColorModel
java.awt.print.PageFormat
java.beans.PropertyChangeEvent
java.beans.PropertyChangeListener
java.beans.PropertyChangeSupport
java.lang.annotation.Annotation
java.lang.reflect.AccessibleObject
java.lang.reflect.Field
java.lang.reflect.Type
java.nio.ByteBuffer
java.nio.CharBuffer
java.nio.channels.Channel
java.nio.charset.Charset
java.nio.file.Path
java.sql.Connection
java.sql.Date
java.sql.Time
java.time.Instant
java.time.LocalDate
java.time.Period
java.util.concurrent.FutureTask
java.util.function.IntBinaryOperator
java.util.function.IntConsumer
java.util.function.IntPredicate
java.util.function.IntSupplier
java.util.function.IntToDoubleFunction
java.util.function.IntToLongFunction
java.util.function.IntUnaryOperator
java.util.stream.IntStream
java.util.zip.ZipOutputStream
javax.accessibility.Accessible
javax.accessibility.AccessibleStateSet
javax.crypto.SecretKey
javax.net.SocketFactory
javax.net.ssl.HttpsURLConnection
javax.net.ssl.SSLSocketFactory
javax.print.attribute.HashPrintRequestAttributeSet
javax.print.attribute.standard.MediaSizeName
javax.print.attribute.standard.MediaPrintableArea
javax.print.attribute.standard.DialogTypeSelection
javax.print.attribute.standard.OrientationRequested
javax.print.attribute.standard.Chromaticity
javax.print.attribute.standard.JobName
javax.print.attribute.standard.JobSheets
javax.print.attribute.standard.Copies
javax.print.attribute.standard.PrintQuality
javax.print.attribute.standard.PrinterResolution
javax.security.auth.Destroyable
javax.swing.Icon
javax.swing.JMenu
javax.swing.plaf.ComponentUI
javax.swing.plaf.basic.BasicButtonUI
javax.swing.plaf.basic.BasicProgressBarUI
javax.swing.plaf.basic.BasicScrollBarUI
javax.swing.plaf.basic.BasicTreeUI
javax.swing.table.AbstractTableModel
javax.swing.table.DefaultTableCellRenderer
javax.swing.table.DefaultTableColumnModel
javax.swing.table.TableCellEditor
javax.swing.table.TableCellRenderer
javax.swing.table.TableColumn
javax.swing.table.TableModel
javax.swing.tree.DefaultTreeCellRenderer
javax.swing.tree.DefaultTreeModel
javax.swing.tree.ExpandVetoException
javax.swing.tree.TreeCellRenderer
javax.swing.tree.TreeModel
javax.swing.tree.TreeNode
javax.swing.tree.TreePath
javax.swing.undo.UndoManager
javax.swing.undo.UndoableEdit
org.antlr.stringtemplate.StringTemplate
org.jfree.base.config.ModifiableConfiguration
org.jfree.chart.ChartPanel
org.jfree.chart.LegendItemSource
org.jfree.chart.axis.ValueAxis
org.jfree.chart.block.AbstractBlock
org.jfree.chart.block.Arrangement
org.jfree.chart.block.Block
org.jfree.chart.block.BlockContainer
org.jfree.chart.entity.EntityCollection
org.jfree.chart.event.AxisChangeListener
org.jfree.chart.event.MarkerChangeListener
org.jfree.chart.event.PlotChangeListener
org.jfree.chart.event.RendererChangeListener
org.jfree.chart.imagemap.ToolTipTagFragmentGenerator
org.jfree.chart.imagemap.URLTagFragmentGenerator
org.jfree.chart.plot.DefaultDrawingSupplier
org.jfree.chart.renderer.PaintScale
org.jfree.chart.title.Title
org.jfree.data.DomainInfo
org.jfree.data.KeyedValue
org.jfree.data.KeyedValues
org.jfree.data.Range
org.jfree.data.RangeInfo
org.jfree.data.Value
org.jfree.data.category.CategoryDataset
org.jfree.data.category.DefaultCategoryDataset
org.jfree.data.contour.ContourDataset
org.jfree.data.function.Function2D
org.jfree.data.general.PieDataset
org.jfree.data.statistics.BoxAndWhiskerCategoryDataset
org.jfree.data.time.Day
org.jfree.data.time.RegularTimePeriod
org.jfree.data.time.TimeSeries
org.jfree.data.time.TimeSeriesCollection
org.jfree.data.xy.AbstractIntervalXYDataset
org.jfree.data.xy.OHLCDataset
org.jfree.data.xy.TableXYDataset
org.jfree.data.xy.XYDataset
org.jfree.data.xy.XYSeries
org.jfree.date.MonthConstants
org.jfree.date.SerialDate
org.jfree.text.TextBox
org.jfree.ui.Drawable
org.jfree.util.PublicCloneable
org.jfree.util.UnitType
 """

type_conversions = {
    'void': 'None',
    'boolean': 'bool',
    'byte': 'int',
    'char': 'str',
    'double': 'float',
    'float': 'float',
    'int': 'int',
    'long': 'int',
    'short': 'int',
    "__builtin__.object": "object",
    'java.math.BigDecimal': 'float',
    'java.math.BigInteger': 'int',
    'java.lang.Boolean': 'bool',
    'java.lang.Exception': 'Exception',
    'java.lang.Integer': 'int',
    'java.lang.Iterable': 'Iterable',
    'java.lang.Long': 'int',
    'java.lang.Object': 'object',
    # 'java.lang.Runnable': 'Callable',
    'java.lang.String': 'str',
    'java.util.AbstractMap': 'Mapping',
    'java.util.ArrayList': 'list',
    'java.util.HashMap': 'dict',
    'java.util.Hashtable': 'dict',
    'java.util.Iterator': 'Iterator',
    'java.util.List': 'list',
    'java.util.Map': 'dict',
    'java.util.Set': 'set',
    'java.util.Vector': 'list',
    'java.util.WeakHashMap': 'Mapping',
    'org.python.core.PyObject': 'object',
}


def remove_basic_types(t):
    # type: (str) -> Iterator[str]
    if "." in t and not t.startswith("typing."):
        yield t


def remove_container(t):
    # type: (str) -> Iterator[str]
    wrapper, _, t = t.partition("[")
    yield wrapper
    if not t:
        return
    assert t.endswith("]"), t
    t = t[:-1]
    if "," in t:
        if "[" not in t or t.index(",") < t.index("["):
            for part in t.split(",", 1):
                for next_t in remove_container(part.strip()):
                    yield next_t
            return
        t, _, remainder = t.rpartition("]")
        for next_t in remove_container(t + "]"):
            yield next_t
        if remainder:
            assert remainder.startswith(","), (remainder, t)
            for next_t in remove_container(remainder[1:].strip()):
                yield next_t
        return
    for next_t in remove_container(t):
        yield next_t


def imported_types_only(all_types):
    # type: (List[str]) -> Iterator[str]
    for t in all_types:
        t = t.replace("'", "")
        for contained in remove_container(t):
            for non_basic in remove_basic_types(contained):
                yield non_basic


class Class(object):
    def __init__(self, module, cls, name=None):  # type: (Module, type, Optional[str]) -> None
        self.module = module
        self.cls = cls
        self.name = name or self.cls.__name__

    def find_type_dependencies(self):
        try:
            for name, value in inspect.getmembers(self.cls):
                if (inspect.ismethod(value) or inspect.isroutine(value)) and not inspect.ismethoddescriptor(value):
                    for t in self.find_method_type_dependencies(name, value):
                        yield t
                elif inspect.isclass(value) and value.__module__ == self.module.name:
                    if '{}${}'.format(self.name, name) in str(value):
                        # self.build_class(name, cls)
                        for t in Class(self.module, value, name).find_type_dependencies():
                            yield t
        except TypeError:
            pass

    def find_method_type_dependencies(self, name, method):
        if name in ('__new__', '__subclasshook__'):
            return
        if not hasattr(method, 'argslist'):
            return
        arg_list = method.argslist[0]
        if arg_list:
            m = arg_list.method
            if arg_list.declaringClass != self.cls:
                return
            unknown_types = set()
            all_types = [t.partition(":")[2].strip() for t in self.module.parse_parameters(m, unknown_types, set())]
            all_types.append(self.module.parse_return_type(m, unknown_types, set()))
            for t in imported_types_only(all_types):
                yield t


class Module(object):
    def __init__(self, name):  # type: (str) -> None
        self.module = importlib.import_module(name)
        self.found_type_dependencies = False
        self.other_modules = set()
        self.has_generic = set()
        self.has_types = False  # Until we find them
        self._submodules = None

    @property
    def name(self):  # type: () -> str
        return self.module.__name__

    @property
    def submodule_names(self):  # type: () -> Set[str]
        if self._submodules is None:
            self._submodules = set()
            try:
                for member_name, member in inspect.getmembers(self.module):
                    if member_name == "__name__":
                        continue
                    if "<java package " in str(member):
                        self._submodules.add(member.__name__)
            except:
                pass
        return self._submodules

    @property
    def visible_classes(self):  # type: () -> Dict[str, type]
        try:
            return {
                name: member
                for name, member in inspect.getmembers(self.module)
                if (
                        inspect.isclass(member)
                        and member.__module__ == self.name
                        # and "{}.{}".format(member.__module__, name) not in type_conversions
                )
            }
        except:
            return {}

    def find_type_dependencies(self):  # type: () -> Iterator[str]
        self.found_type_dependencies = True
        for cls in self.visible_classes.values():
            for t in Class(self, cls).find_type_dependencies():
                sub = t.partition(".")[0]
                if sub not in ("com", "java", "javax", "org"):
                    if "{}.{}".format(self.name, sub) in self.submodule_names:
                        t = "{}.{}".format(self.name, t)
                yield t

    def convert_type(self, p, unknown_types, completed_output_classes):
        # type: (str, Set[str], Set[str]) -> str
        p = p.strip()
        if '<' in p:
            container, contents = p.partition('<')[::2]
            contents = contents[:-1]
            self.has_types = True
            if container in ('java.util.Map', 'java.util.HashMap', 'java.util.Hashtable'):
                parts = contents.split(',')
                if len(parts) != 2:
                    raise Exception('Expected {} to have 2 parts'.format(parts))
                return 'typing.Dict[{},{}]'.format(self.convert_type(parts[0], unknown_types, completed_output_classes), self.convert_type(parts[1], unknown_types, completed_output_classes))
            if container in ('java.util.List', 'java.util.ArrayList'):
                return 'typing.List[{}]'.format(self.convert_type(contents, unknown_types, completed_output_classes))
            if container == 'java.util.Collection':
                return 'typing.Sequence[{}]'.format(self.convert_type(contents, unknown_types, completed_output_classes))
            if container == 'java.util.Set':
                return 'typing.Set[{}]'.format(self.convert_type(contents, unknown_types, completed_output_classes))
            if container == 'java.util.Iterator':
                return 'typing.Iterator[{}]'.format(self.convert_type(contents, unknown_types, completed_output_classes))
            if container == 'java.lang.Iterable':
                return 'typing.Iterable[{}]'.format(self.convert_type(contents, unknown_types, completed_output_classes))
            if container in ('java.util.Comparable', 'java.util.Comparator'):
                return 'typing.Callable[[{0}, {0}], int]'.format(self.convert_type(contents, unknown_types, completed_output_classes))
            return 'typing.Any'
            # raise NotImplementedError('Conversion for {}'.format(p))
        if p.endswith('[]'):
            p = self.convert_type(p[:-2], unknown_types, completed_output_classes)
            self.has_types = True
            return 'typing.List[{}]'.format(p)
        if '$' in p:
            return 'str'
        result = type_conversions.get(p)
        if result is not None:
            if result in typing:
                result = "typing.{}".format(result)
                self.has_types = True
            return result
        if "." in p:
            if p.startswith(self.name + '.'):
                type_name = p[len(self.name) + 1:]
                if '.' in type_name:
                    sub_module = type_name.rpartition('.')[0]
                    if '{}.{}'.format(self.name, sub_module) in AllModules.names():
                        self.other_modules.add(sub_module)
                        return type_name
                    else:
                        return "'{}'".format(type_name)
                return type_name if type_name in completed_output_classes else "'{}'".format(type_name)
            else:
                for m in AllModules.modules():
                    other_module = p.rpartition('.')[0]
                    if m.name == other_module:
                        self.other_modules.add(other_module)
                        return p  # if modules.index(m) > modules.index(self.module) else "'{}'".format(type_name)
        if p.startswith("?super"):
            p = p[6:]
        elif p.startswith("?extends"):
            p = p[8:]
        if len(p) == 1 and p.isupper():
            self.has_generic.add(p)
        elif len(p) == 1 and p == "?":
            p = "T"
            self.has_generic.add(p)
        else:
            unknown_types.add(p)
        return "'{}'".format(p)

    def convert_parameter_type(self, p, used_names, unknown_types, completed_output_classes):
        # type: (str, Set[str], Set[str], Set[str]) -> str
        full_type = self.convert_type(p, unknown_types, completed_output_classes)
        t = full_type.replace("'", '')
        if 'A' <= t[0] <= 'Z':
            proposed_name = t[0].lower() + t[1:]
        else:
            proposed_name = t[0]
        proposed_name = proposed_name.partition('[')[0]
        name = proposed_name
        next_index = 2
        while proposed_name in used_names:
            proposed_name = '{}{}'.format(name, next_index)
            next_index += 1
        used_names.add(proposed_name)

        return '{}: {}'.format(proposed_name, full_type)

    def parse_parameters(self, method, unknown_types, completed_output_classes):
        # type: (Any, Set[str], Set[str]) -> List[str]
        if method.parameterCount == 0:
            return []
        used_names = set()
        params = fixup_container_strings(str(method.annotatedParameterTypes).partition('[')[2][:-2])
        if method.parameterCount == 1:
            return [self.convert_parameter_type(params, used_names, unknown_types, completed_output_classes)]
        params = params.split(', ')
        if len(params) != method.parameterCount:
            # See if we broke up a generic
            while len(params) > method.parameterCount:
                for i in range(len(params) - 1):
                    if params[i].count("<") > params[i].count(">") and params[i+1].count(">") > params[i+1].count("<"):
                        params[i:i+2] = ["{}, {}".format(params[i], params[i+1])]
                        break
                else:
                    break
            if len(params) != method.parameterCount:
                raise Exception('{}: {} should have {} entries'.format(method, params, method.parameterCount))
        return [self.convert_parameter_type(param, used_names, unknown_types, completed_output_classes) for param in params]

    def parse_return_type(self, method, unknown_types, completed_output_classes):
        result = fixup_container_strings(str(method.annotatedReturnType))
        return self.convert_type(result, unknown_types, completed_output_classes)


class AllModules(object):
    _initialized = False
    _modules = {  # type: Dict[str, Optional[Module]]
        name: None for name in starter_modules
    }

    @classmethod
    def _unimported(cls):
        return [name for name, value in cls._modules.items() if value is None]

    @classmethod
    def _import_all(cls):
        while not cls._initialized:
            cls._initialized = True
            for name in cls._unimported():
                module = Module(name)
                cls._modules[name] = module
                for submodule_name in module.submodule_names:
                    if submodule_name not in cls._modules:
                        cls._initialized = False
                        cls._modules[submodule_name] = None

    @classmethod
    def names(cls):
        cls._import_all()
        return set(cls._modules.keys())

    @classmethod
    def modules(cls):  # type: () -> List[Module]
        cls._import_all()
        return list(cls._modules.values())

    @classmethod
    def find_module(cls, name):  # type: (str) -> Module | None
        mod_name, _, class_name = name.rpartition(".")
        if class_name[0].isupper():
            module = cls.find_module(mod_name)
            if module is not None and class_name not in dir(module.module):
                module.found_type_dependencies = False
                importlib.import_module(name)
        else:
            module = cls._modules.get(name)
            if not module:
                try:
                    module = Module(name)
                except ImportError:
                    return None
                cls._modules[name] = module
        return module


write_folder = os.path.realpath("Downloads/MoneyDancePython")
try:
    os.makedirs(write_folder)
except OSError:
    pass
print("Writing to", write_folder)


class Builder:
    def __init__(self):
        self.indent = 0
        self.result = ''
        self.index = 0

    def add(self, line='', post_indent=0):
        self.index += 1
        if self.result:
            self.result += '\n'
        self.result += '{}{}'.format(' ' * (4*self.indent), line)
        self.indent += post_indent


class ModulePYIWriter(object):
    def __init__(self, module):  # type: (Module) -> None
        self.module = module
        self.classes_dict = self.module.visible_classes
        self.classes = list(self.classes_dict.values())
        self.class_local_bases = {}
        self.class_external_bases = {}
        self.started_output_classes = set()
        self.completed_output_classes = set()
        self.builder = Builder()
        self.unknown_types = set()
        self.lines = []

        self.register_bases_in_module(inspect.getclasstree(self.classes, False))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.lines:
            parts = self.module.name.split('.')
            path = write_folder
            if not os.path.exists(path):
                os.makedirs(path)
            for part in parts:
                path = os.path.join(path, part)
                if not os.path.exists(path):
                    os.makedirs(path)
                    with open(os.path.join(path, '__init__.pyi'), 'w'):
                        pass
            filename = os.path.join(path, '__init__.pyi')
            # print 'Writing {}'.format(filename)
            with open(filename, 'w') as f:
                if self.module.has_generic:
                    self.module.has_types = True
                if self.module.has_types:
                    f.write('import typing\n')
                for other in sorted(self.module.other_modules):
                    f.write('import {}\n'.format(other))
                f.write('\n')
                if self.module.has_generic:
                    for v in sorted(self.module.has_generic):
                        f.write('{0} = typing.TypeVar("{0}")\n'.format(v))
                    f.write("\n")
                f.write('\n')
                for line in self.lines:
                    f.write(line)
                    f.write('\n')

    def add(self, line='', post_indent=0):
        # type: (str, int) -> None
        self.builder.add(line, post_indent)

    def _write(self, line):
        self.lines.append(line)

    def write_all(self):
        for c in sorted(self.classes, key=lambda x: x.__name__):
            self.write_class(c)

    def register_bases_in_module(self, items):
        for item in items:
            if isinstance(item, tuple):
                cls, bases = item
                if cls.__module__ == self.module.name:
                    bases = tuple(filter(lambda x: x.__module__ == self.module.name, item[1]))
                    if bases:
                        self.class_local_bases[cls] = bases
                    bases = tuple(filter(lambda x: x.__module__ != self.module.name and x.__name__ != 'Object', item[1]))
                    if bases:
                        self.class_external_bases[cls] = bases
            elif isinstance(item, list):
                self.register_bases_in_module(item)

    def write_class(self, c):
        if c not in self.started_output_classes:
            self.started_output_classes.add(c)
            bases = self.class_local_bases.get(c, [])
            for base in bases:
                self.write_class(base)
            name = c.__name__
            self.build_class(name, c, bases, self.class_external_bases.get(c, []))
            self._write(self.builder.result)
            self.builder = Builder()
            self.completed_output_classes.add(name)

    def build_class(self, class_name, cls, bases=None, external_bases=None):
        # type: (str, type, List[type], List[type]) -> None

        if "$" in class_name:
            for outer in class_name.split("$")[:-1]:
                self.add('class {}(object):'.format(outer), post_indent=1)
            class_name = class_name.rpartition("$")[2]
        bases = bases or []
        external_bases = external_bases or []
        full_name = "{}.{}".format(self.module.name, class_name)
        class_method_info = class_info.get(full_name, {})
        extra_lines = class_extra_lines.get(full_name)

        base = ''
        if bases or external_bases:
            internal_parts = [bc.__name__.replace("$", ".") for bc in bases]
            external_parts = [self.module.convert_type('.'.join([bc.__module__, bc.__name__]), self.unknown_types, self.completed_output_classes) for bc in external_bases]
            base = '(' + ', '.join(internal_parts + external_parts) + ')'
        self.add('class {}{}:'.format(class_name, base), post_indent=1)
        def_index = self.builder.index

        start_index = self.builder.index
        try:
            for name, value in inspect.getmembers(cls, lambda k: not inspect.isclass(k) and not inspect.ismethod(k) and not inspect.isroutine(k)):
                if name == '__doc__' and value is None:
                    continue
                if not value or isinstance(value, (int, float, unicode, str, bool)):
                    v = repr(value)
                else:
                    v = str(value)
                    type_ref = "${}".format(class_name)
                    v = v.replace(type_ref, ".{}".format(class_name))
                    m = mem_ref_regex.search(v)
                    if m:
                        i = v[:m.endpos].rfind("@")
                        v = v[:i]
                    v = repr(v)
                    if v.startswith("'<"):
                        v = v.replace("$", ".")
                        v, _, tail = v.partition(" at 0x")
                        if tail:
                            v += ">'"
                        if v.startswith("'<reflected field public "):
                            v = v.partition("public ")[2]
                            for prefix in ("final", "transient"):
                                if v.startswith(prefix):
                                    v = v.partition(" ")[2]
                            v = v.partition(" ")[0]
                            v = self.module.convert_type(v, self.unknown_types, self.completed_output_classes)
                            self.add('{}: {}'.format(name, v))
                            continue
                self.add('{} = {}'.format(name, v))
        except TypeError:
            pass
        if start_index != self.builder.index:
            self.add()

        start_index = self.builder.index
        if extra_lines:
            for line in extra_lines:
                self.add(line)
            self.add()
        try:
            for name, method in inspect.getmembers(cls, lambda k: (inspect.ismethod(k) or inspect.isroutine(k)) and not inspect.ismethoddescriptor(k)):
                self.build_method(cls, class_method_info, name, method)
        except TypeError:
            pass
        if start_index != self.builder.index:
            self.add()

        start_index = self.builder.index
        try:
            for name, cls in inspect.getmembers(cls, lambda k: inspect.isclass(k) and k.__module__ == self.module.name):
                if '{}${}'.format(class_name, name) in str(cls):
                    self.build_class(name, cls)
        except TypeError:
            pass
        if start_index != self.builder.index:
            self.add()

        if def_index == self.builder.index:
            self.add('pass')
            self.add()

        self.builder.indent -= 1

    def build_method(self, cls, class_method_info, name, method):
        if name in ('__new__', '__subclasshook__'):
            return
        arg_list = method.argslist[0] if hasattr(method, 'argslist') else None
        comment = ''
        selfer = 'self'
        returner = ' -> None'
        paramer = ''
        staticer = ''
        method_info = class_method_info.get(name)
        if arg_list:
            m = arg_list.method
            if arg_list.declaringClass != cls:
                return
            paramer = ", ".join(self.module.parse_parameters(m, self.unknown_types, self.completed_output_classes))
            if method_info:
                paramer = method_info.params
            selfer = 'self, ' if paramer else 'self'
            if name != '__init__':
                if hasattr(arg_list, 'isStatic') and arg_list.isStatic:
                    selfer = ''
                    staticer = '@staticmethod'
                returner = ' -> {}'.format(self.module.parse_return_type(m, self.unknown_types, self.completed_output_classes))

        if staticer:
            self.add(staticer)
        self.add('def {}({}{}){}: ...'.format(name, selfer, paramer, returner))
        if comment:
            self.add(comment)
        self.add()


def fixup_container_strings(params):
    i = params.find('<')
    while i >= 0:
        e = params.find('>', i + 1)
        params = params[:i] + params[i:e].replace(' ', '') + params[e:]
        i = params.find('<', e)
    return params


def add_unknown_types():
    found_types = set()
    for module in sorted(AllModules.modules(), key=lambda x: x.__name__):
        found_types.update(module.find_type_dependencies())
    for t in sorted(found_types):
        if starter_modules_regex.match(t):
            AllModules.find_module(t)
            print("-", t)


def ensure_specific_imports():
    for line in specific_imports_to_ensure.splitlines():
        line = " ".join(line.strip().split()).replace(", ", ",").partition(" #")[0]
        if not line or line[0] == "#":
            continue
        if " " not in line:
            AllModules.find_module(line)
        elif line.startswith("import"):
            AllModules.find_module(line.partition(" ")[2])
        elif line.startswith("from"):
            line = line.partition(" ")[2]
            module_name, _, classes = line.strip().partition(" import ")
            for class_name in classes.split(","):
                AllModules.find_module("{}.{}".format(module_name, class_name))
    for module_name in class_extra_lines.keys():
        AllModules.find_module(module_name)
    for module_name in class_info.keys():
        AllModules.find_module(module_name)


# noinspection PyTypeChecker
def main():
    all_unknown_types = set()
    ensure_specific_imports()
    # add_unknown_types()
    for module in sorted(AllModules.modules()):
        with ModulePYIWriter(module) as writer:
            writer.write_all()
            all_unknown_types.update(writer.unknown_types)
    with open(os.path.join(write_folder, 'moneydance.pyi'), 'w') as f:
        f.write("""import com.moneydance.apps.md.controller
import com.infinitekind.moneydance.model
import com.moneydance.apps.md.view.gui
import com.moneydance.apps.md.view.gui.bot

moneydance = com.moneydance.apps.md.controller.Main()
moneydance_data = com.infinitekind.moneydance.model.AccountBook()
moneydance_ui = com.moneydance.apps.md.view.gui.MoneydanceGUI(moneydance)
moneybot = com.moneydance.apps.md.view.gui.bot.PythonInterface(moneydance_ui, moneydance_data)
""")

    if all_unknown_types:
        print('Unknown ({}):'.format(len(all_unknown_types)))
        for u in sorted(all_unknown_types):
            print(' ', u)


main()
