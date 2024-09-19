microcode = '''
def macroop EVEX_VPSLLD_XMM_XMM_XMM {
    gem5_avx_sll_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPSLLD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sll_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPSLLD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sll_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPSLLD_XMM_XMM_I {
    gem5_avx_sll_epu32_immi xmm, xmmm, imm, size=4, ext=XMM
};

def macroop EVEX_VPSLLD_XMM_M_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLD_XMM_P_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLD_YMM_YMM_XMM {
    gem5_avx_sll_epu32 ymm1, ymm2, xmmm, size=4, ext=YMM
};

def macroop EVEX_VPSLLD_YMM_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sll_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPSLLD_YMM_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sll_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPSLLD_YMM_YMM_I {
    gem5_avx_sll_epu32_immi ymm, ymmm, imm, size=4, ext=YMM
};

def macroop EVEX_VPSLLD_YMM_M_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLD_YMM_P_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLD_ZMM_ZMM_XMM {
    gem5_avx_sll_epu32 zmm1, zmm2, xmmm, size=4, ext=ZMM
};

def macroop EVEX_VPSLLD_ZMM_ZMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sll_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPSLLD_ZMM_ZMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sll_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPSLLD_ZMM_ZMM_I {
    gem5_avx_sll_epu32_immi zmm, zmmm, imm, size=4, ext=ZMM
};

def macroop EVEX_VPSLLD_ZMM_M_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLD_ZMM_P_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLQ_XMM_XMM_XMM {
    gem5_avx_sll_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPSLLQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sll_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPSLLQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sll_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPSLLQ_XMM_XMM_I {
    gem5_avx_sll_epu64_immi xmm, xmmm, imm, size=8, ext=XMM
};

def macroop EVEX_VPSLLQ_XMM_M_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLQ_XMM_P_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLQ_YMM_YMM_XMM {
    gem5_avx_sll_epu64 ymm1, ymm2, xmmm, size=8, ext=YMM
};

def macroop EVEX_VPSLLQ_YMM_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sll_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPSLLQ_YMM_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sll_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPSLLQ_YMM_YMM_I {
    gem5_avx_sll_epu64_immi ymm, ymmm, imm, size=8, ext=YMM
};

def macroop EVEX_VPSLLQ_YMM_M_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLQ_YMM_P_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLQ_ZMM_ZMM_XMM {
    gem5_avx_sll_epu64 zmm1, zmm2, xmmm, size=8, ext=ZMM
};

def macroop EVEX_VPSLLQ_ZMM_ZMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sll_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPSLLQ_ZMM_ZMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sll_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPSLLQ_ZMM_ZMM_I {
    gem5_avx_sll_epu64_immi zmm, zmmm, imm, size=8, ext=ZMM
};

def macroop EVEX_VPSLLQ_ZMM_M_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLQ_ZMM_P_I {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSLLDQ_XMM_XMM_I {
    gem5_avx_slli_epu128i xmm, xmmm, imm, size=16, ext=XMM
};

def macroop EVEX_VPSLLDQ_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_slli_epu128i xmm, uvec1, imm, size=16, ext=XMM
};

def macroop EVEX_VPSLLDQ_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_slli_epu128i xmm, uvec1, imm, size=16, ext=XMM
};

def macroop EVEX_VPSLLDQ_YMM_YMM_I {
    gem5_avx_slli_epu128i ymm, ymmm, imm, size=32, ext=YMM
};

def macroop EVEX_VPSLLDQ_YMM_M_I {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_slli_epu128i ymm, uvec1, imm, size=32, ext=YMM
};

def macroop EVEX_VPSLLDQ_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_slli_epu128i ymm, uvec1, imm, size=32, ext=YMM
};

def macroop EVEX_VPSLLDQ_ZMM_ZMM_I {
    gem5_avx_slli_epu128i zmm, zmmm, imm, size=64, ext=ZMM
};

def macroop EVEX_VPSLLDQ_ZMM_M_I {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_slli_epu128i zmm, uvec1, imm, size=64, ext=ZMM
};

def macroop EVEX_VPSLLDQ_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_slli_epu128i zmm, uvec1, imm, size=64, ext=ZMM
};

'''
