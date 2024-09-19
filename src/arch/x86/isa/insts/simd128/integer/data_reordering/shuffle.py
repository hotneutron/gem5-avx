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
def macroop PSHUFB_XMM_XMM {
    gem5_mm_shuffle_epi8 xmm, xmm, xmmm, size=1, ext=0
};

def macroop PSHUFB_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_shuffle_epi8 xmm, xmm, uvec1, size=1, ext=0
};

def macroop PSHUFB_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_shuffle_epi8 xmm, xmm, uvec1, size=1, ext=0
};

def macroop PSHUFD_XMM_XMM_I {
    gem5_mm_shuffle_epi32 xmm, xmmm, size=4, ext="IMMEDIATE"
};

def macroop PSHUFD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_shuffle_epi32 xmm, uvec1, size=4, ext="IMMEDIATE"
};

def macroop PSHUFD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_shuffle_epi32 xmm, uvec1, size=4, ext="IMMEDIATE"
};

def macroop PSHUFHW_XMM_XMM_I {
    gem5_mm_shufflehi_epi16 xmm, xmmm, size=2, ext=imm
};

def macroop PSHUFHW_XMM_M_I {
    ldvec128hi0 uvec1, seg, sib, "DISPLACEMENT + 8", dataSize=8
    gem5_mm_shufflehi_epi16 xmm, uvec1, size=2, ext=imm
};

def macroop PSHUFHW_XMM_P_I {
    rdip t7
    ldvec128hi0 uvec1, seg, riprel, "DISPLACEMENT + 8", dataSize=8
    gem5_mm_shufflehi_epi16 xmm, uvec1, size=2, ext=imm
};

def macroop PSHUFLW_XMM_XMM_I {
    gem5_mm_shufflelo_epi16 xmm, xmmm, size=2, ext=imm
};

def macroop PSHUFLW_XMM_M_I {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_mm_shufflelo_epi16 xmm, uvec1, size=2, ext=imm
};

def macroop PSHUFLW_XMM_P_I {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, "DISPLACEMENT", dataSize=8
    gem5_mm_shufflelo_epi16 xmm, uvec1, size=2, ext=imm
};
'''
