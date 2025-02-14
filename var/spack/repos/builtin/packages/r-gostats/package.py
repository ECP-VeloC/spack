# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RGostats(RPackage):
    """Tools for manipulating GO and microarrays

       A set of tools for interacting with GO and microarray data. A variety of
       basic manipulation tools for graphs, hypothesis testing and other simple
       calculations."""

    homepage = "https://bioconductor.org/packages/GOstats"
    git      = "https://git.bioconductor.org/packages/GOstats.git"

    version('2.56.0', commit='8f988c3b4b1ce7e05626aae8956004c7bbdd6f3a')
    version('2.50.0', commit='ee13f84341988d537a5485dcdcfb71f69e6e4930')
    version('2.48.0', commit='5db7020f4bab725cd729b32bd1d5e819b31f2485')
    version('2.46.0', commit='489d7a437488f77c3010f6212f3b81f4e240cd17')
    version('2.44.0', commit='fc64ca2aa37c52656d396d6e46611f39d6efd48a')
    version('2.42.0', commit='8b29709064a3b66cf1d963b2be0c996fb48c873e')

    depends_on('r+X', type=('build', 'run'))
    depends_on('r@2.10:', type=('build', 'run'))
    depends_on('r-biobase@1.15.29:', type=('build', 'run'))
    depends_on('r-category@2.3.26:', type=('build', 'run'))
    depends_on('r-category@2.43.2:', when='@2.44.0:', type=('build', 'run'))
    depends_on('r-graph@1.15.15:', when='@2.42.0', type=('build', 'run'))
    depends_on('r-graph', when='@2.44.0:', type=('build', 'run'))
    depends_on('r-annotationdbi@0.0.89:', type=('build', 'run'))
    depends_on('r-go-db@1.13.0:', type=('build', 'run'))
    depends_on('r-rbgl', type=('build', 'run'))
    depends_on('r-annotate@1.13.2:', type=('build', 'run'))
    depends_on('r-annotationforge', type=('build', 'run'))
    depends_on('r-rgraphviz', when='@2.44.0:', type=('build', 'run'))
