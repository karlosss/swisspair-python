# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

set(CMAKE_CXX_STANDARD 20)

# Scikit-build-core sets these values for you, or you can just hard-code the
# name and version.
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

add_link_options(-lgmp)

add_subdirectory(swisspair)
add_subdirectory(swisspair/gmpwrap)
add_subdirectory(swisspair/Minimum-Cost-Perfect-Matching)

# Find the module development requirements (requires FindPython from 3.17 or
# scikit-build-core's built-in backport)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

# Add a library using FindPython's tooling (pybind11 also provides a helper like
# this)
python_add_library(pyswisspair MODULE src/bindings.cpp WITH_SOABI)
target_link_libraries(pyswisspair PRIVATE pybind11::headers)
target_link_libraries(pyswisspair PRIVATE swisspair)
target_link_libraries(pyswisspair PRIVATE gmpwrap)
target_link_libraries(pyswisspair PRIVATE mincostpmatch)

# This is passing in the version as a define just as an example
target_compile_definitions(pyswisspair PRIVATE VERSION_INFO=${PROJECT_VERSION})

# The install directory is the output (wheel) directory
install(TARGETS pyswisspair DESTINATION swisspair)
