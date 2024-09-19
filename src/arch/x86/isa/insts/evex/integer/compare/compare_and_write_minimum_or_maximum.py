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
def macroop EVEX_VPMINUB_XMM_XMM_XMM {
    gem5_avx_min_epu8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop EVEX_VPMINUB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPMINUB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPMINUB_YMM_YMM_YMM {
    gem5_avx_min_epu8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop EVEX_VPMINUB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPMINUB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPMINUB_ZMM_ZMM_ZMM {
    gem5_avx_min_epu8 zmm1, zmm2, zmmm, size=1, ext=ZMM
};

def macroop EVEX_VPMINUB_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_min_epu8 zmm1, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPMINUB_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_min_epu8 zmm1, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPMINSD_XMM_XMM_XMM {
    gem5_avx_min_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPMINSD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMINSD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMINSD_YMM_YMM_YMM {
    gem5_avx_min_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPMINSD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMINSD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMINSD_ZMM_ZMM_ZMM {
    gem5_avx_min_epi32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPMINSD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_min_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMINSD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_min_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMINSQ_XMM_XMM_XMM {
    gem5_avx_min_epi64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPMINSQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPMINSQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPMINSQ_YMM_YMM_YMM {
    gem5_avx_min_epi64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPMINSQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPMINSQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPMINSQ_ZMM_ZMM_ZMM {
    gem5_avx_min_epi64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPMINSQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_min_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPMINSQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_min_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPMAXSD_XMM_XMM_XMM {
    gem5_avx_max_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPMAXSD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMAXSD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMAXSD_YMM_YMM_YMM {
    gem5_avx_max_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPMAXSD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMAXSD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMAXSD_ZMM_ZMM_ZMM {
    gem5_avx_max_epi32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPMAXSD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_max_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMAXSD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_max_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMAXSQ_XMM_XMM_XMM {
    gem5_avx_max_epi64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPMAXSQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPMAXSQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPMAXSQ_YMM_YMM_YMM {
    gem5_avx_max_epi64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPMAXSQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPMAXSQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPMAXSQ_ZMM_ZMM_ZMM {
    gem5_avx_max_epi64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPMAXSQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_max_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPMAXSQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_max_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPMAXSD_XMM_XMM_XMM_K {
    gem5_mask_max_epi32 xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPMAXSD_XMM_XMM_M_K  {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_max_epi32 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPMAXSD_XMM_XMM_P_K  {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_max_epi32 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPMAXSD_YMM_YMM_YMM_K  {
    gem5_mask_max_epi32 ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPMAXSD_YMM_YMM_M_K  {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_max_epi32 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPMAXSD_YMM_YMM_P_K  {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_max_epi32 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPMAXSD_ZMM_ZMM_ZMM_K  {
    gem5_mask_max_epi32 zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPMAXSD_ZMM_ZMM_M_K  {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_max_epi32 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPMAXSD_ZMM_ZMM_P_K  {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_max_epi32 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPMAXSQ_XMM_XMM_XMM_K {
    gem5_mask_max_epi64 xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPMAXSQ_XMM_XMM_M_K  {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_max_epi64 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPMAXSQ_XMM_XMM_P_K  {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_max_epi64 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPMAXSQ_YMM_YMM_YMM_K  {
    gem5_mask_max_epi64 ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPMAXSQ_YMM_YMM_M_K  {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_max_epi64 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPMAXSQ_YMM_YMM_P_K  {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_max_epi64 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPMAXSQ_ZMM_ZMM_ZMM_K  {
    gem5_mask_max_epi64 zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPMAXSQ_ZMM_ZMM_M_K  {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_max_epi64 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPMAXSQ_ZMM_ZMM_P_K  {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_max_epi64 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

'''
