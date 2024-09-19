microcode = '''
def macroop EVEX_VFMADD132SS_XMM_XMM_XMM {
    gem5_avx_fmadd132_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop EVEX_VFMADD132SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fmadd132_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VFMADD132SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fmadd132_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VFMADD132SD_XMM_XMM_XMM {
    gem5_avx_fmadd132_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop EVEX_VFMADD132SD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fmadd132_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VFMADD132SD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fmadd132_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VFMADD213SS_XMM_XMM_XMM {
    gem5_avx_fmadd213_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop EVEX_VFMADD213SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fmadd213_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VFMADD213SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fmadd213_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VFMADD213SD_XMM_XMM_XMM {
    gem5_avx_fmadd213_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop EVEX_VFMADD213SD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fmadd213_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VFMADD213SD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fmadd213_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VFMADD231SS_XMM_XMM_XMM {
    gem5_avx_fmadd231_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop EVEX_VFMADD231SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fmadd231_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VFMADD231SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fmadd231_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VFMADD231SD_XMM_XMM_XMM {
    gem5_avx_fmadd231_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop EVEX_VFMADD231SD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fmadd231_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VFMADD231SD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fmadd231_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

'''

template_code = '''
def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_%(reg_type)s {
    gem5_avx_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, %(reg)sm, size=%(elem_size)s, ext=%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_M {
    ldvec%(size_bits)s uvec1, seg, sib, disp, dataSize=%(size_bytes)s
    gem5_avx_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, size=%(elem_size)s, ext=%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_P {
    rdip t7
    ldvec%(size_bits)s uvec1, seg, riprel, disp, dataSize=%(size_bytes)s
    gem5_avx_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, size=%(elem_size)s, ext=%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_%(reg_type)s_K {
    gem5_mask_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, %(reg)sm, opmask=opmask, size=%(elem_size)s, ext=%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_M_K {
    ldvec%(size_bits)s uvec1, seg, sib, disp, dataSize=%(size_bytes)s
    gem5_mask_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, opmask=opmask, size=%(elem_size)s, ext=%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_P_K {
    rdip t7
    ldvec%(size_bits)s uvec1, seg, riprel, disp, dataSize=%(size_bytes)s
    gem5_mask_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, opmask=opmask, size=%(elem_size)s, ext=%(reg_type)s
};
'''

list1=[('VFMADD132PS','fmadd132_ps','4'),
       ('VFMADD213PS','fmadd213_ps','4'),
       ('VFMADD231PS','fmadd231_ps','4'),
       ('VFMADD132PD','fmadd132_pd','8'),
       ('VFMADD213PD','fmadd213_pd','8'),
       ('VFMADD231PD','fmadd231_pd','8')]
list2=[('XMM','128','16'),('YMM','256','32'),('ZMM','512','64')]

for (instruction,func_name,elem_size) in list1:
    for (reg_type,size_bits,size_bytes) in list2:
        microcode += template_code % {"instruction": instruction,
                                      "func_name": func_name,
                                      "elem_size": elem_size,
                                      "reg_type": reg_type,
                                      "reg": reg_type.lower(),
                                      "size_bits": size_bits,
                                      "size_bytes": size_bytes}
