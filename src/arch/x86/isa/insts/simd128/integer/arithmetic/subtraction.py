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
def macroop PSUBB_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=1, ext=0
};

def macroop PSUBB_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=1, ext=0
};

def macroop PSUBB_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=1, ext=0
};

def macroop PSUBW_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=2, ext=0
};

def macroop PSUBW_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=2, ext=0
};

def macroop PSUBW_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=2, ext=0
};

def macroop PSUBD_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=4, ext=0
};

def macroop PSUBD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=4, ext=0
};

def macroop PSUBD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=4, ext=0
};

def macroop PSUBQ_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=8, ext=0
};

def macroop PSUBQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=8, ext=0
};

def macroop PSUBQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=8, ext=0
};

def macroop PSUBSB_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=1, ext = "2 |" + Signed
};

def macroop PSUBSB_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=1, ext = "2 |" + Signed
};

def macroop PSUBSB_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=1, ext = "2 |" + Signed
};

def macroop PSUBSW_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=2, ext = "2 |" + Signed
};

def macroop PSUBSW_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=2, ext = "2 |" + Signed
};

def macroop PSUBSW_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=2, ext = "2 |" + Signed
};

def macroop PSUBUSB_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=1, ext=2
};

def macroop PSUBUSB_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=1, ext=2
};

def macroop PSUBUSB_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=1, ext=2
};

def macroop PSUBUSW_XMM_XMM {
    sse_msubi xmm, xmm, xmmm, size=2, ext=2
};

def macroop PSUBUSW_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=2, ext=2
};

def macroop PSUBUSW_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    sse_msubi xmm, xmm, uvec1, size=2, ext=2
};

def macroop PHSUBW_XMM_XMM {
    gem5_mm_hsub_epi16 xmm, xmm, xmmm, size=2, ext=0
};

def macroop PHSUBW_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_hsub_epi16 xmm, xmm, uvec1, size=2, ext=0
};

def macroop PHSUBW_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_hsub_epi16 xmm, xmm, uvec1, size=2, ext=0
};

def macroop PHSUBD_XMM_XMM {
    gem5_mm_hsub_epi32 xmm, xmm, xmmm, size=4, ext=0
};

def macroop PHSUBD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_hsub_epi32 xmm, xmm, uvec1, size=4, ext=0
};

def macroop PHSUBD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_hsub_epi32 xmm, xmm, uvec1, size=4, ext=0
};

def macroop PHSUBSW_XMM_XMM {
    gem5_mm_hsubs_epi16 xmm, xmm, xmmm, size=2, ext=0
};

def macroop PHSUBSW_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_hsubs_epi16 xmm, xmm, uvec1, size=2, ext=0
};

def macroop PHSUBSW_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_hsubs_epi16 xmm, xmm, uvec1, size=2, ext=0
};

'''
