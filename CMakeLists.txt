# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_INSTALL_RPATH $ORIGIN)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Scikit-build-core sets these values for you, or you can just hard-code the
# name and version.
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

add_subdirectory(src/swisspair_cpp)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

python_add_library(_swisspair MODULE src/bindings.cpp WITH_SOABI)
target_link_libraries(_swisspair PRIVATE pybind11::headers)
target_link_libraries(_swisspair PRIVATE swisspair)

# The install directory is the output (wheel) directory
install(TARGETS _swisspair DESTINATION swisspair)
install(TARGETS swisspair DESTINATION swisspair)
install(TARGETS gmpwrap DESTINATION swisspair)
install(TARGETS mincostpmatch DESTINATION swisspair)
