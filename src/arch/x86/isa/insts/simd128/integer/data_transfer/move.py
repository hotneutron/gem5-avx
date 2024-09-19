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
def macroop MOVQ_XMM_XMM {
    gem5_mm_move_epi64 xmm, xmmm
};

def macroop MOVQ_XMM_R {
   sse_mov2vec xmm, regm, srcSize=dsz, destSize=8
};

def macroop MOVQ_XMM_M {
    ldvec128lo0 xmm, seg, sib, disp, dataSize=8
};

def macroop MOVQ_XMM_P {
    rdip t7
    ldvec128lo0 xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVQ_R_XMM {
    sse_mov2int reg, xmmm, size=dsz
};

def macroop MOVQ_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop MOVQ_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVDQ2Q_MMX_XMM {
    gem5_mm_movepi64_pi64 mmx, xmmm, dataSize=8
};

def macroop MOVQ2DQ_XMM_MMX {
    sse_mov_fp2vec xmm, mmxm, dataSize=8
};

def macroop MOVDQA_XMM_XMM {
    sse_mov_vec2vec xmm, xmmm
};

def macroop MOVDQA_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQA_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQA_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQA_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQU_XMM_XMM {
    sse_mov_vec2vec xmm, xmmm
};

def macroop MOVDQU_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQU_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQU_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVDQU_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop LDDQU_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop LDDQU_XMM_P {
    rdip t7
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};
'''
