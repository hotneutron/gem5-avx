# Copyright (c) 2007 The Hewlett-Packard Development Company
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

microcode = '''
def macroop EVEX_VPMOVQD_XMM_XMM {
    gem5_avx_cvtepi64_epi32 xmm, xmmm, srcSize=8, destSize=4, ext=XMM
};

def macroop EVEX_VPMOVQD_M_XMM {
    gem5_avx_cvtepi64_epi32 uvec1, xmmm, srcSize=8, destSize=4, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPMOVQD_P_XMM {
    gem5_avx_cvtepi64_epi32 uvec1, xmmm, srcSize=8, destSize=4, ext=XMM
    rdip t7
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPMOVQD_XMM_YMM {
    gem5_avx_cvtepi64_epi32 xmm, ymmm, srcSize=8, destSize=4, ext=YMM
};

def macroop EVEX_VPMOVQD_M_YMM {
    gem5_avx_cvtepi64_epi32 uvec1, ymmm, srcSize=8, destSize=4, ext=YMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPMOVQD_P_YMM {
    gem5_avx_cvtepi64_epi32 uvec1, ymmm, srcSize=8, destSize=4, ext=YMM
    rdip t7
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPMOVQD_YMM_ZMM {
    gem5_avx_cvtepi64_epi32 ymm, zmmm, srcSize=8, destSize=4, ext=ZMM
};

def macroop EVEX_VPMOVQD_M_ZMM {
    gem5_avx_cvtepi64_epi32 uvec1, zmmm, srcSize=8, destSize=4, ext=ZMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VPMOVQD_P_ZMM {
    gem5_avx_cvtepi64_epi32 uvec1, zmmm, srcSize=8, destSize=4, ext=ZMM
    rdip t7
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VPMOVSXDQ_XMM_XMM {
    gem5_avx_cvtepi32_epi64 xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMOVSXDQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMOVSXDQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMOVSXDQ_YMM_XMM {
    gem5_avx_cvtepi32_epi64 ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMOVSXDQ_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMOVSXDQ_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMOVSXDQ_ZMM_YMM {
    gem5_avx_cvtepi32_epi64 zmm, ymmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMOVSXDQ_ZMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepi32_epi64 zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMOVSXDQ_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepi32_epi64 zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMOVZXDQ_XMM_XMM {
    gem5_avx_cvtepu32_epi64 xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMOVZXDQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMOVZXDQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMOVZXDQ_YMM_XMM {
    gem5_avx_cvtepu32_epi64 ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMOVZXDQ_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMOVZXDQ_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMOVZXDQ_ZMM_YMM {
    gem5_avx_cvtepu32_epi64 zmm, ymmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMOVZXDQ_ZMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepu32_epi64 zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMOVZXDQ_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepu32_epi64 zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

'''
