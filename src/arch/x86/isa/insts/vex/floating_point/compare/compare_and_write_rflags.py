microcode = '''
def macroop VEX_VUCOMISS_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=4
};

def macroop VEX_VUCOMISS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop VEX_VUCOMISS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop VEX_VUCOMISD_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=8
};

def macroop VEX_VUCOMISD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop VEX_VUCOMISD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop VEX_VCOMISS_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=4
};

def macroop VEX_VCOMISS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop VEX_VCOMISS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop VEX_VCOMISD_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=8
};

def macroop VEX_VCOMISD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop VEX_VCOMISD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop VEX_VPCMPISTRI_XMM_XMM_I {
    gem5_mm_cmpistri1 xmm, xmmm, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPISTRI_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpistri1 xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPISTRI_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpistri1 xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPISTRM_XMM_XMM_I {
    gem5_mm_cmpistrm xmm, xmmm, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPISTRM_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpistrm xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPISTRM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpistrm xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPESTRI_XMM_XMM_I {
    gem5_mm_cmpestri1 xmm, xmmm, size=16, ext="IMMEDIATE"
};

def macroop VEX_VPCMPESTRI_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpestri1 xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPESTRI_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpestri1 xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPESTRM_XMM_XMM_I {
    gem5_mm_cmpestrm xmm, xmmm, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPESTRM_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_cmpestrm xmm, uvec1, size=16, ext="IMMEDIATE" 
};

def macroop VEX_VPCMPESTRM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_mm_cmpestrm xmm, uvec1, size=16, ext="IMMEDIATE" 
};

'''
