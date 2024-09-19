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
def macroop UCOMISS_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=4
};

def macroop UCOMISS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop UCOMISS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop UCOMISD_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=8
};

def macroop UCOMISD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop UCOMISD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop COMISS_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=4
};

def macroop COMISS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop COMISS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop COMISD_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=8
};

def macroop COMISD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop COMISD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop PCMPISTRI_XMM_XMM_I {
    gem5_mm_cmpistri1 xmm, xmmm, size=16, ext="IMMEDIATE"
};

def macroop PCMPISTRI_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpistri1 xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPISTRI_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpistri1 xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPISTRM_XMM_XMM_I {
    gem5_mm_cmpistrm xmm, xmmm, size=16, ext="IMMEDIATE"
};

def macroop PCMPISTRM_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpistrm xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPISTRM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpistrm xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPESTRI_XMM_XMM_I {
    gem5_mm_cmpestri1 xmm, xmmm, size=16, ext="IMMEDIATE"
};

def macroop PCMPESTRI_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpestri1 xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPESTRI_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpestri1 xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPESTRM_XMM_XMM_I {
    gem5_mm_cmpestrm xmm, xmmm, size=16, ext="IMMEDIATE"
};

def macroop PCMPESTRM_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpestrm xmm, uvec1, size=16, ext="IMMEDIATE"
};

def macroop PCMPESTRM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpestrm xmm, uvec1, size=16, ext="IMMEDIATE"
};

'''
