cmake_minimum_required(VERSION 2.8)

include(RezBuild)

file(GLOB h_files "*.h")

rez_install_files(
    ${h_files}
    DESTINATION include
)

