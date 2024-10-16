# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_INSTALL_RPATH $ORIGIN)

execute_process (
    COMMAND bash -c "pybind11-config --cmakedir"
    OUTPUT_VARIABLE CMAKEDIR
)

add_definitions(-Dpybind11_DIR="${CMAKEDIR}")

# Scikit-build-core sets these values for you, or you can just hard-code the
# name and version.
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

add_link_options(-lgmp)

add_subdirectory(src/swisspair_cpp)
add_subdirectory(src/swisspair_cpp/gmpwrap)
add_subdirectory(src/swisspair_cpp/Minimum-Cost-Perfect-Matching)

# Find the module development requirements (requires FindPython from 3.17 or
# scikit-build-core's built-in backport)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

# Add a library using FindPython's tooling (pybind11 also provides a helper like
# this)
python_add_library(_swisspair MODULE src/bindings.cpp WITH_SOABI)
target_link_libraries(_swisspair PRIVATE pybind11::headers)
target_link_libraries(_swisspair PRIVATE swisspair)
target_link_libraries(_swisspair PRIVATE gmpwrap)
target_link_libraries(_swisspair PRIVATE mincostpmatch)

# This is passing in the version as a define just as an example
target_compile_definitions(_swisspair PRIVATE VERSION_INFO=${PROJECT_VERSION})

# The install directory is the output (wheel) directory
install(TARGETS _swisspair DESTINATION swisspair)
install(TARGETS swisspair DESTINATION swisspair)
install(TARGETS gmpwrap DESTINATION swisspair)
install(TARGETS mincostpmatch DESTINATION swisspair)
