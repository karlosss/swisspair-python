cmake_minimum_required(VERSION 3.15...3.27)

set(CMAKE_CXX_STANDARD 20)

project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_MACOSX_RPATH 1)
    set(CMAKE_INSTALL_RPATH @loader_path)
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(CMAKE_INSTALL_RPATH $ORIGIN)
endif()

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_subdirectory(src/swisspair_cpp)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

python_add_library(_swisspair MODULE src/bindings.cpp WITH_SOABI)
target_link_libraries(_swisspair PRIVATE pybind11::headers)
target_link_libraries(_swisspair PRIVATE swisspair)

install(TARGETS _swisspair DESTINATION swisspair)
install(TARGETS swisspair DESTINATION swisspair)
install(TARGETS gmpwrap DESTINATION swisspair)
install(TARGETS mincostpmatch DESTINATION swisspair)
