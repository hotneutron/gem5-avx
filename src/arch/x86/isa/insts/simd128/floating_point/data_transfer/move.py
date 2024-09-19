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
def macroop MOVAPS_XMM_M {
    # Check low address.
    ldvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop MOVAPS_XMM_P {
    rdip t7
    # Check low address.
    ldvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop MOVAPS_M_XMM {
    # Check low address.
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop MOVAPS_P_XMM {
    rdip t7
    # Check low address.
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop MOVAPS_XMM_XMM {
    # Check low address.
    sse_mov_vec2vec xmm, xmmm, dataSize=16
};

def macroop MOVAPD_XMM_XMM {
    sse_mov_vec2vec xmm, xmmm, dataSize=16
};

def macroop MOVAPD_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVAPD_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVAPD_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVAPD_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPS_XMM_XMM {
    sse_mov_vec2vec xmm, xmmm, dataSize=16
};

def macroop MOVUPS_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPS_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPS_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPS_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPD_XMM_XMM {
    sse_mov_vec2vec xmm, xmmm, dataSize=16
};

def macroop MOVUPD_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPD_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPD_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop MOVUPD_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop MOVHPS_XMM_M {
    ldvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop MOVHPS_XMM_P {
    rdip t7
    ldvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVHPS_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop MOVHPS_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVHPD_XMM_M {
    ldvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop MOVHPD_XMM_P {
    rdip t7
    ldvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVHPD_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop MOVHPD_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVLPS_XMM_M {
    ldvec128lo0 xmm, seg, sib, disp, dataSize=8
};

def macroop MOVLPS_XMM_P {
    rdip t7
    ldvec128lo0 xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVLPS_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop MOVLPS_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVLPD_XMM_M {
    ldvec128lo0 xmm, seg, sib, disp, dataSize=8
};

def macroop MOVLPD_XMM_P {
    rdip t7
    ldvec128lo0 xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVLPD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop MOVLPD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVHLPS_XMM_XMM {
    gem5_mm_movehl_ps  xmm, xmmm, dataSize=16
};

def macroop MOVLHPS_XMM_XMM {
    gem5_mm_movelh_ps xmm, xmmm, dataSize=16
};

def macroop MOVSS_XMM_XMM {
    gem5_mm_move_ss xmm, xmmm, dataSize=4
};

def macroop MOVSS_XMM_M {
    gem5_mm_load_ss xmm, seg, sib, disp, dataSize=4
};

def macroop MOVSS_XMM_P {
    rdip t7
    gem5_mm_load_ss xmm, seg, riprel, disp, dataSize=4
};

def macroop MOVSS_M_XMM {
    gem5_mm_store_ss xmm, seg, sib, disp, dataSize=4
};

def macroop MOVSS_P_XMM {
    rdip t7
    gem5_mm_store_ss xmm, seg, riprel, disp, dataSize=4
};

def macroop MOVSD_XMM_M {
    gem5_mm_load_sd xmm, seg, sib, disp, dataSize=8
};

def macroop MOVSD_XMM_P {
# PUHAHA. need to merge
    rdip t7
    gem5_mm_load_sd xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVSD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop MOVSD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop MOVSD_XMM_XMM {
    gem5_mm_move_sd xmm, xmmm, dataSize=8
};
'''
