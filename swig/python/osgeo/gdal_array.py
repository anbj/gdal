# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _gdal_array
else:
    import _gdal_array

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


from . import gdal
class VirtualMem(object):
    r"""Proxy of C++ CPLVirtualMemShadow class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _gdal_array.delete_VirtualMem

    def GetAddr(self) -> "void":
        r"""GetAddr(VirtualMem self)"""
        return _gdal_array.VirtualMem_GetAddr(self)

    def Pin(self, start_offset: "size_t"=0, nsize: "size_t"=0, bWriteOp: "int"=0) -> "void":
        r"""Pin(VirtualMem self, size_t start_offset=0, size_t nsize=0, int bWriteOp=0)"""
        return _gdal_array.VirtualMem_Pin(self, start_offset, nsize, bWriteOp)

# Register VirtualMem in _gdal_array:
_gdal_array.VirtualMem_swigregister(VirtualMem)


def _StoreLastException() -> "void":
    r"""_StoreLastException()"""
    return _gdal_array._StoreLastException()

def TermProgress_nocb(dfProgress: "double", pszMessage: "char const *"=None, pData: "void *"=None) -> "int":
    r"""TermProgress_nocb(double dfProgress, char const * pszMessage=None, void * pData=None) -> int"""
    return _gdal_array.TermProgress_nocb(dfProgress, pszMessage, pData)
TermProgress = _gdal_array.TermProgress


def OpenNumPyArray(psArray: "PyArrayObject *", binterleave: "bool") -> "GDALDatasetShadow *":
    r"""OpenNumPyArray(PyArrayObject * psArray, bool binterleave) -> Dataset"""
    return _gdal_array.OpenNumPyArray(psArray, binterleave)

def OpenMultiDimensionalNumPyArray(psArray: "PyArrayObject *") -> "GDALDatasetShadow *":
    r"""OpenMultiDimensionalNumPyArray(PyArrayObject * psArray) -> Dataset"""
    return _gdal_array.OpenMultiDimensionalNumPyArray(psArray)

def GetArrayFilename(psArray: "PyArrayObject *") -> "retStringAndCPLFree *":
    r"""GetArrayFilename(PyArrayObject * psArray) -> retStringAndCPLFree *"""
    return _gdal_array.GetArrayFilename(psArray)

def BandRasterIONumPy(band: "Band", bWrite: "int", xoff: "double", yoff: "double", xsize: "double", ysize: "double", psArray: "PyArrayObject *", buf_type: "GDALDataType", resample_alg: "GDALRIOResampleAlg", callback: "GDALProgressFunc"=0, callback_data: "void *"=None) -> "CPLErr":
    r"""BandRasterIONumPy(Band band, int bWrite, double xoff, double yoff, double xsize, double ysize, PyArrayObject * psArray, GDALDataType buf_type, GDALRIOResampleAlg resample_alg, GDALProgressFunc callback=0, void * callback_data=None) -> CPLErr"""
    return _gdal_array.BandRasterIONumPy(band, bWrite, xoff, yoff, xsize, ysize, psArray, buf_type, resample_alg, callback, callback_data)

def DatasetIONumPy(ds: "Dataset", bWrite: "int", xoff: "double", yoff: "double", xsize: "double", ysize: "double", psArray: "PyArrayObject *", buf_type: "GDALDataType", resample_alg: "GDALRIOResampleAlg", callback: "GDALProgressFunc"=0, callback_data: "void *"=None, binterleave: "bool"=True, band_list: "int"=0) -> "CPLErr":
    r"""DatasetIONumPy(Dataset ds, int bWrite, double xoff, double yoff, double xsize, double ysize, PyArrayObject * psArray, GDALDataType buf_type, GDALRIOResampleAlg resample_alg, GDALProgressFunc callback=0, void * callback_data=None, bool binterleave=True, int band_list=0) -> CPLErr"""
    return _gdal_array.DatasetIONumPy(ds, bWrite, xoff, yoff, xsize, ysize, psArray, buf_type, resample_alg, callback, callback_data, binterleave, band_list)

def MDArrayIONumPy(bWrite: "bool", mdarray: "GDALMDArrayHS *", psArray: "PyArrayObject *", nDims1: "int", nDims3: "int", buffer_datatype: "GDALExtendedDataTypeHS *") -> "CPLErr":
    r"""MDArrayIONumPy(bool bWrite, GDALMDArrayHS * mdarray, PyArrayObject * psArray, int nDims1, int nDims3, GDALExtendedDataTypeHS * buffer_datatype) -> CPLErr"""
    return _gdal_array.MDArrayIONumPy(bWrite, mdarray, psArray, nDims1, nDims3, buffer_datatype)

def _RecordBatchAsNumpy(recordBatchPtr: "VoidPtrAsLong", schemaPtr: "VoidPtrAsLong", pointerArrayKeeper: "PyObject *") -> "PyObject *":
    r"""_RecordBatchAsNumpy(VoidPtrAsLong recordBatchPtr, VoidPtrAsLong schemaPtr, PyObject * pointerArrayKeeper) -> PyObject *"""
    return _gdal_array._RecordBatchAsNumpy(recordBatchPtr, schemaPtr, pointerArrayKeeper)

def VirtualMemGetArray(virtualmem: "VirtualMem") -> "int":
    r"""VirtualMemGetArray(VirtualMem virtualmem)"""
    return _gdal_array.VirtualMemGetArray(virtualmem)

def RATValuesIONumPyWrite(poRAT: "RasterAttributeTable", nField: "int", nStart: "int", psArray: "PyArrayObject *") -> "CPLErr":
    r"""RATValuesIONumPyWrite(RasterAttributeTable poRAT, int nField, int nStart, PyArrayObject * psArray) -> CPLErr"""
    return _gdal_array.RATValuesIONumPyWrite(poRAT, nField, nStart, psArray)

def RATValuesIONumPyRead(poRAT: "RasterAttributeTable", nField: "int", nStart: "int", nLength: "int") -> "PyObject *":
    r"""RATValuesIONumPyRead(RasterAttributeTable poRAT, int nField, int nStart, int nLength) -> PyObject *"""
    return _gdal_array.RATValuesIONumPyRead(poRAT, nField, nStart, nLength)

import numpy

from osgeo import gdalconst
from osgeo import gdal
gdal.AllRegister()

codes = {gdalconst.GDT_Byte: numpy.uint8,
         gdalconst.GDT_Int8: numpy.int8,
         gdalconst.GDT_UInt16: numpy.uint16,
         gdalconst.GDT_Int16: numpy.int16,
         gdalconst.GDT_UInt32: numpy.uint32,
         gdalconst.GDT_Int32: numpy.int32,
         gdalconst.GDT_UInt64: numpy.uint64,
         gdalconst.GDT_Int64: numpy.int64,
         gdalconst.GDT_Float32: numpy.float32,
         gdalconst.GDT_Float64: numpy.float64,
         gdalconst.GDT_CInt16: numpy.complex64,
         gdalconst.GDT_CInt32: numpy.complex64,
         gdalconst.GDT_CFloat32:  numpy.complex64,
         gdalconst.GDT_CFloat64: numpy.complex128}


def OpenArray(array, prototype_ds=None, interleave='band'):

    interleave = interleave.lower()
    if interleave == 'band':
        interleave = True
    elif interleave == 'pixel':
        interleave = False
    else:
        raise ValueError('Interleave should be band or pixel')

    ds = OpenNumPyArray(array, interleave)

    if ds is not None and prototype_ds is not None:
        if type(prototype_ds).__name__ == 'str':
            prototype_ds = gdal.Open(prototype_ds)
        if prototype_ds is not None:
            CopyDatasetInfo(prototype_ds, ds)

    return ds


def flip_code(code):
    if isinstance(code, (numpy.dtype, type)):
# since several things map to complex64 we must carefully select
# the opposite that is an exact match (ticket 1518)
        if code == numpy.complex64:
            return gdalconst.GDT_CFloat32

        for key, value in codes.items():
            if value == code:
                return key
        return None
    else:
        try:
            return codes[code]
        except KeyError:
            return None

def NumericTypeCodeToGDALTypeCode(numeric_type):
    if not isinstance(numeric_type, (numpy.dtype, type)):
        raise TypeError("Input must be a type")
    return flip_code(numeric_type)

def GDALTypeCodeToNumericTypeCode(gdal_code):
    return flip_code(gdal_code)

def _RaiseException():
    if gdal.GetUseExceptions():
        _StoreLastException()
        raise RuntimeError(gdal.GetLastErrorMsg())

def LoadFile(filename, xoff=0, yoff=0, xsize=None, ysize=None,
             buf_xsize=None, buf_ysize=None, buf_type=None,
             resample_alg=gdal.GRIORA_NearestNeighbour,
             callback=None, callback_data=None, interleave='band',
             band_list=None):
    ds = gdal.Open(filename)
    if ds is None:
        raise ValueError("Can't open "+filename+"\n\n"+gdal.GetLastErrorMsg())

    return DatasetReadAsArray(ds, xoff, yoff, xsize, ysize,
                              buf_xsize=buf_xsize, buf_ysize=buf_ysize, buf_type=buf_type,
                              resample_alg=resample_alg,
                              callback=callback, callback_data=callback_data,
                              interleave=interleave,
                              band_list=band_list)

def SaveArray(src_array, filename, format="GTiff", prototype=None, interleave='band'):
    driver = gdal.GetDriverByName(format)
    if driver is None:
        raise ValueError("Can't find driver "+format)

    return driver.CreateCopy(filename, OpenArray(src_array, prototype, interleave))


def DatasetReadAsArray(ds, xoff=0, yoff=0, win_xsize=None, win_ysize=None, buf_obj=None,
                       buf_xsize=None, buf_ysize=None, buf_type=None,
                       resample_alg=gdal.GRIORA_NearestNeighbour,
                       callback=None, callback_data=None, interleave='band',
                       band_list=None):
    """Pure python implementation of reading a chunk of a GDAL file
    into a numpy array.  Used by the gdal.Dataset.ReadAsArray method."""

    if win_xsize is None:
        win_xsize = ds.RasterXSize
    if win_ysize is None:
        win_ysize = ds.RasterYSize

    if band_list is None:
        band_list = list(range(1, ds.RasterCount + 1))

    interleave = interleave.lower()
    if interleave == 'band':
        interleave = True
        xdim = 2
        ydim = 1
        banddim = 0
    elif interleave == 'pixel':
        interleave = False
        xdim = 1
        ydim = 0
        banddim = 2
    else:
        raise ValueError('Interleave should be band or pixel')

    nbands = len(band_list)
    if nbands == 0:
        return None

    if nbands == 1:
        return BandReadAsArray(ds.GetRasterBand(band_list[0]), xoff, yoff, win_xsize, win_ysize,
                               buf_xsize=buf_xsize, buf_ysize=buf_ysize, buf_type=buf_type,
                               buf_obj=buf_obj,
                               resample_alg=resample_alg,
                               callback=callback,
                               callback_data=callback_data)

    if buf_obj is None:
        if buf_xsize is None:
            buf_xsize = win_xsize
        if buf_ysize is None:
            buf_ysize = win_ysize
        if buf_type is None:
            buf_type = ds.GetRasterBand(band_list[0]).DataType
            for idx in range(1, nbands):
                band_index = band_list[idx]
                if buf_type != ds.GetRasterBand(band_index).DataType:
                    buf_type = gdalconst.GDT_Float32

        typecode = GDALTypeCodeToNumericTypeCode(buf_type)
        if typecode is None:
            buf_type = gdalconst.GDT_Float32
            typecode = numpy.float32
        else:
            buf_type = NumericTypeCodeToGDALTypeCode(typecode)

        if buf_type == gdalconst.GDT_Byte and ds.GetRasterBand(1).GetMetadataItem('PIXELTYPE', 'IMAGE_STRUCTURE') == 'SIGNEDBYTE':
            typecode = numpy.int8
        buf_shape = (nbands, buf_ysize, buf_xsize) if interleave else (buf_ysize, buf_xsize, nbands)
        buf_obj = numpy.empty(buf_shape, dtype=typecode)

    else:
        if len(buf_obj.shape) != 3:
            raise ValueError('Array should have 3 dimensions')

        shape_buf_xsize = buf_obj.shape[xdim]
        shape_buf_ysize = buf_obj.shape[ydim]
        if buf_xsize is not None and buf_xsize != shape_buf_xsize:
            raise ValueError('Specified buf_xsize not consistent with array shape')
        if buf_ysize is not None and buf_ysize != shape_buf_ysize:
            raise ValueError('Specified buf_ysize not consistent with array shape')
        if buf_obj.shape[banddim] != nbands:
            raise ValueError('Dimension %d of array should have size %d to store bands)' % (banddim, nbands))

        datatype = NumericTypeCodeToGDALTypeCode(buf_obj.dtype.type)
        if not datatype:
            raise ValueError("array does not have corresponding GDAL data type")
        if buf_type is not None and buf_type != datatype:
            raise ValueError("Specified buf_type not consistent with array type")
        buf_type = datatype

    if DatasetIONumPy(ds, 0, xoff, yoff, win_xsize, win_ysize,
                      buf_obj, buf_type, resample_alg, callback, callback_data,
                      interleave, band_list) != 0:
        _RaiseException()
        return None

    return buf_obj


def DatasetWriteArray(ds, array, xoff=0, yoff=0,
                      band_list=None,
                      interleave='band',
                      resample_alg=gdal.GRIORA_NearestNeighbour,
                      callback=None, callback_data=None):
    """Pure python implementation of writing a chunk of a GDAL file
    from a numpy array.  Used by the gdal.Dataset.WriteArray method."""

    if band_list is None:
        band_list = list(range(1, ds.RasterCount + 1))

    interleave = interleave.lower()
    if interleave == 'band':
        interleave = True
        xdim = 2
        ydim = 1
        banddim = 0
    elif interleave == 'pixel':
        interleave = False
        xdim = 1
        ydim = 0
        banddim = 2
    else:
        raise ValueError('Interleave should be band or pixel')

    if len(band_list) == 1:
        if array is None or (len(array.shape) != 2 and len(array.shape) != 3):
            raise ValueError("expected array of dim 2 or 3")
        if len(array.shape) == 3:
            if array.shape[banddim] != 1:
                raise ValueError("expected size of dimension %d should be 1" % banddim)
            array = array[banddim]

        return BandWriteArray(ds.GetRasterBand(band_list[0]),
                              array,
                              xoff=xoff, yoff=yoff, resample_alg=resample_alg,
                              callback=callback, callback_data=callback_data)

    if array is None or len(array.shape) != 3:
        raise ValueError("expected array of dim 3")

    xsize = array.shape[xdim]
    ysize = array.shape[ydim]

    if xsize + xoff > ds.RasterXSize or ysize + yoff > ds.RasterYSize:
        raise ValueError("array larger than output file, or offset off edge")
    if array.shape[banddim] != len(band_list):
        raise ValueError('Dimension %d of array should have size %d to store bands)' % (banddim, len(band_list)))

    datatype = NumericTypeCodeToGDALTypeCode(array.dtype.type)

# if we receive some odd type, like int64, try casting to a very
# generic type we do support (#2285)
    if not datatype:
        gdal.Debug('gdal_array', 'force array to float64')
        array = array.astype(numpy.float64)
        datatype = NumericTypeCodeToGDALTypeCode(array.dtype.type)

    if not datatype:
        raise ValueError("array does not have corresponding GDAL data type")

    ret = DatasetIONumPy(ds, 1, xoff, yoff, xsize, ysize,
                         array, datatype, resample_alg, callback, callback_data,
                         interleave, band_list)
    if ret != 0:
        _RaiseException()
    return ret


def BandReadAsArray(band, xoff=0, yoff=0, win_xsize=None, win_ysize=None,
                    buf_xsize=None, buf_ysize=None, buf_type=None, buf_obj=None,
                    resample_alg=gdal.GRIORA_NearestNeighbour,
                    callback=None, callback_data=None):
    """Pure python implementation of reading a chunk of a GDAL file
    into a numpy array.  Used by the gdal.Band.ReadAsArray method."""

    if win_xsize is None:
        win_xsize = band.XSize
    if win_ysize is None:
        win_ysize = band.YSize

    if buf_obj is None:
        if buf_xsize is None:
            buf_xsize = win_xsize
        if buf_ysize is None:
            buf_ysize = win_ysize
        if buf_type is None:
            buf_type = band.DataType

        typecode = GDALTypeCodeToNumericTypeCode(buf_type)
        if typecode is None:
            buf_type = gdalconst.GDT_Float32
            typecode = numpy.float32
        else:
            buf_type = NumericTypeCodeToGDALTypeCode(typecode)

        if buf_type == gdalconst.GDT_Byte and band.GetMetadataItem('PIXELTYPE', 'IMAGE_STRUCTURE') == 'SIGNEDBYTE':
            typecode = numpy.int8
        buf_obj = numpy.empty([buf_ysize, buf_xsize], dtype=typecode)

    else:
        if len(buf_obj.shape) not in (2, 3):
            raise ValueError("expected array of dimension 2 or 3")

        if len(buf_obj.shape) == 2:
            shape_buf_xsize = buf_obj.shape[1]
            shape_buf_ysize = buf_obj.shape[0]
        else:
            if buf_obj.shape[0] != 1:
                raise ValueError("expected size of first dimension should be 0")
            shape_buf_xsize = buf_obj.shape[2]
            shape_buf_ysize = buf_obj.shape[1]
        if buf_xsize is not None and buf_xsize != shape_buf_xsize:
            raise ValueError('Specified buf_xsize not consistent with array shape')
        if buf_ysize is not None and buf_ysize != shape_buf_ysize:
            raise ValueError('Specified buf_ysize not consistent with array shape')

        datatype = NumericTypeCodeToGDALTypeCode(buf_obj.dtype.type)
        if not datatype:
            raise ValueError("array does not have corresponding GDAL data type")
        if buf_type is not None and buf_type != datatype:
            raise ValueError("Specified buf_type not consistent with array type")
        buf_type = datatype

    if BandRasterIONumPy(band, 0, xoff, yoff, win_xsize, win_ysize,
                         buf_obj, buf_type, resample_alg, callback, callback_data) != 0:
        _RaiseException()
        return None

    return buf_obj

def BandWriteArray(band, array, xoff=0, yoff=0,
                   resample_alg=gdal.GRIORA_NearestNeighbour,
                   callback=None, callback_data=None):
    """Pure python implementation of writing a chunk of a GDAL file
    from a numpy array.  Used by the gdal.Band.WriteArray method."""

    if array is None or len(array.shape) != 2:
        raise ValueError("expected array of dim 2")

    xsize = array.shape[1]
    ysize = array.shape[0]

    if xsize + xoff > band.XSize or ysize + yoff > band.YSize:
        raise ValueError("array larger than output file, or offset off edge")

    datatype = NumericTypeCodeToGDALTypeCode(array.dtype.type)

# if we receive some odd type, like int64, try casting to a very
# generic type we do support (#2285)
    if not datatype:
        gdal.Debug('gdal_array', 'force array to float64')
        array = array.astype(numpy.float64)
        datatype = NumericTypeCodeToGDALTypeCode(array.dtype.type)

    if not datatype:
        raise ValueError("array does not have corresponding GDAL data type")

    ret = BandRasterIONumPy(band, 1, xoff, yoff, xsize, ysize,
                             array, datatype, resample_alg, callback, callback_data)
    if ret != 0:
        _RaiseException()
    return ret

def _ExtendedDataTypeToNumPyDataType(dt):
    klass = dt.GetClass()

    if klass == gdal.GEDTC_STRING:
        return numpy.bytes_, dt

    if klass == gdal.GEDTC_NUMERIC:
        buf_type = dt.GetNumericDataType()
        typecode = GDALTypeCodeToNumericTypeCode(buf_type)
        if typecode is None:
            typecode = numpy.float32
            dt = gdal.ExtendedDataType.Create(gdal.GDT_Float32)
        else:
            dt = gdal.ExtendedDataType.Create(NumericTypeCodeToGDALTypeCode(typecode))
        return typecode, dt

    assert klass == gdal.GEDTC_COMPOUND
    names = []
    formats = []
    offsets = []
    for comp in dt.GetComponents():
        names.append(comp.GetName())
        typecode, subdt = _ExtendedDataTypeToNumPyDataType(comp.GetType())
        if subdt != comp.GetType():
            raise Exception("Incompatible datatype")
        formats.append(typecode)
        offsets.append(comp.GetOffset())

    return numpy.dtype({'names': names,
                        'formats': formats,
                        'offsets': offsets,
                        'itemsize': dt.GetSize()}), dt

def ExtendedDataTypeToNumPyDataType(dt):
    typecode, _ = _ExtendedDataTypeToNumPyDataType(dt)
    return typecode

def MDArrayReadAsArray(mdarray,
                        array_start_idx = None,
                        count = None,
                        array_step = None,
                        buffer_datatype = None,
                        buf_obj = None):
    if not array_start_idx:
        array_start_idx = [0] * mdarray.GetDimensionCount()
    if not count:
        count = [ dim.GetSize() for dim in mdarray.GetDimensions() ]
    if not array_step:
        array_step = [1] * mdarray.GetDimensionCount()

    if buf_obj is None:
        if not buffer_datatype:
            buffer_datatype = mdarray.GetDataType()
        typecode, buffer_datatype = _ExtendedDataTypeToNumPyDataType(buffer_datatype)
        buf_obj = numpy.empty(count, dtype=typecode)
    else:
        datatype = NumericTypeCodeToGDALTypeCode(buf_obj.dtype.type)
        if not datatype:
            raise ValueError("array does not have corresponding GDAL data type")

        buffer_datatype = gdal.ExtendedDataType.Create(datatype)

    ret = MDArrayIONumPy(False, mdarray, buf_obj, array_start_idx, array_step, buffer_datatype)
    if ret != 0:
        _RaiseException()
    return buf_obj

def MDArrayWriteArray(mdarray, array,
                        array_start_idx = None,
                        array_step = None):
    if not array_start_idx:
        array_start_idx = [0] * mdarray.GetDimensionCount()
    if not array_step:
        array_step = [1] * mdarray.GetDimensionCount()

    buffer_datatype = mdarray.GetDataType()
    typecode = ExtendedDataTypeToNumPyDataType(buffer_datatype)
    if array.dtype != typecode:
        datatype = NumericTypeCodeToGDALTypeCode(array.dtype.type)

# if we receive some odd type, like int64, try casting to a very
# generic type we do support (#2285)
        if not datatype:
            gdal.Debug('gdal_array', 'force array to float64')
            array = array.astype(numpy.float64)
            datatype = NumericTypeCodeToGDALTypeCode(array.dtype.type)

        if not datatype:
            raise ValueError("array does not have corresponding GDAL data type")

        buffer_datatype = gdal.ExtendedDataType.Create(datatype)

    ret = MDArrayIONumPy(True, mdarray, array, array_start_idx, array_step, buffer_datatype)
    if ret != 0:
        _RaiseException()
    return ret

def RATWriteArray(rat, array, field, start=0):
    """
    Pure Python implementation of writing a chunk of the RAT
    from a numpy array. Type of array is coerced to one of the types
    (int, double, string) supported. Called from RasterAttributeTable.WriteArray
    """
    if array is None:
        raise ValueError("Expected array of dim 1")

# if not the array type convert it to handle lists etc
    if not isinstance(array, numpy.ndarray):
        array = numpy.array(array)

    if array.ndim != 1:
        raise ValueError("Expected array of dim 1")

    if (start + array.size) > rat.GetRowCount():
        raise ValueError("Array too big to fit into RAT from start position")

    if numpy.issubdtype(array.dtype, numpy.integer):
# is some type of integer - coerce to standard int
# TODO: must check this is fine on all platforms
# confusingly numpy.int 64 bit even if native type 32 bit
        array = array.astype(numpy.int32)
    elif numpy.issubdtype(array.dtype, numpy.floating):
# is some type of floating point - coerce to double
        array = array.astype(numpy.double)
    elif numpy.issubdtype(array.dtype, numpy.character):
# cast away any kind of Unicode etc
        array = array.astype(bytes)
    else:
        raise ValueError("Array not of a supported type (integer, double or string)")

    ret = RATValuesIONumPyWrite(rat, field, start, array)
    if ret != 0:
        _RaiseException()
    return ret

def RATReadArray(rat, field, start=0, length=None):
    """
    Pure Python implementation of reading a chunk of the RAT
    into a numpy array. Called from RasterAttributeTable.ReadAsArray
    """
    if length is None:
        length = rat.GetRowCount() - start

    ret = RATValuesIONumPyRead(rat, field, start, length)
    if ret is None:
        _RaiseException()
    return ret

def CopyDatasetInfo(src, dst, xoff=0, yoff=0):
    """
    Copy georeferencing information and metadata from one dataset to another.
    src: input dataset
    dst: output dataset - It can be a ROI -
    xoff, yoff:  dst's offset with respect to src in pixel/line.

    Notes: Destination dataset must have update access.  Certain formats
           do not support creation of geotransforms and/or gcps.

    """

    dst.SetMetadata(src.GetMetadata())



#Check for geo transform
    gt = src.GetGeoTransform()
    if gt != (0, 1, 0, 0, 0, 1):
        dst.SetProjection(src.GetProjectionRef())

        if xoff == 0 and yoff == 0:
            dst.SetGeoTransform(gt)
        else:
            ngt = [gt[0], gt[1], gt[2], gt[3], gt[4], gt[5]]
            ngt[0] = gt[0] + xoff*gt[1] + yoff*gt[2]
            ngt[3] = gt[3] + xoff*gt[4] + yoff*gt[5]
            dst.SetGeoTransform((ngt[0], ngt[1], ngt[2], ngt[3], ngt[4], ngt[5]))

#Check for GCPs
    elif src.GetGCPCount() > 0:

        if (xoff == 0) and (yoff == 0):
            dst.SetGCPs(src.GetGCPs(), src.GetGCPProjection())
        else:
            gcps = src.GetGCPs()
#Shift gcps
            new_gcps = []
            for gcp in gcps:
                ngcp = gdal.GCP()
                ngcp.GCPX = gcp.GCPX
                ngcp.GCPY = gcp.GCPY
                ngcp.GCPZ = gcp.GCPZ
                ngcp.GCPPixel = gcp.GCPPixel - xoff
                ngcp.GCPLine = gcp.GCPLine - yoff
                ngcp.Info = gcp.Info
                ngcp.Id = gcp.Id
                new_gcps.append(ngcp)

            try:
                dst.SetGCPs(new_gcps, src.GetGCPProjection())
            except:
                print("Failed to set GCPs")
                return

    return



