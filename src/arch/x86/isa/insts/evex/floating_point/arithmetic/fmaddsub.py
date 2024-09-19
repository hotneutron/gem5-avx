microcode = '''
'''

template_code = '''
def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_%(reg_type)s {
    gem5_avx_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, %(reg)sm, size=%(elem_size)s, ext=%(ext_arg)s%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_M {
    ldvec%(size_bits)s uvec1, seg, sib, disp, dataSize=%(size_bytes)s
    gem5_avx_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, size=%(elem_size)s, ext=%(ext_arg)s%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_P {
    rdip t7
    ldvec%(size_bits)s uvec1, seg, riprel, disp, dataSize=%(size_bytes)s
    gem5_avx_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, size=%(elem_size)s, ext=%(ext_arg)s%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_%(reg_type)s_K {
    gem5_mask_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, %(reg)sm, opmask=opmask, size=%(elem_size)s, ext=%(ext_arg)s%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_M_K {
    ldvec%(size_bits)s uvec1, seg, sib, disp, dataSize=%(size_bytes)s
    gem5_mask_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, opmask=opmask, size=%(elem_size)s, ext=%(ext_arg)s%(reg_type)s
};

def macroop EVEX_%(instruction)s_%(reg_type)s_%(reg_type)s_P_K {
    rdip t7
    ldvec%(size_bits)s uvec1, seg, riprel, disp, dataSize=%(size_bytes)s
    gem5_mask_%(func_name)s %(reg)s, %(reg)s, %(reg)s2, uvec1, opmask=opmask, size=%(elem_size)s, ext=%(ext_arg)s%(reg_type)s
};
'''

list1=[('VFMADDSUB132PS','fmaddsub132_ps','4',''),
       ('VFMADDSUB213PS','fmaddsub213_ps','4',''),
       ('VFMADDSUB231PS','fmaddsub231_ps','4',''),
       ('VFMADDSUB132PD','fmaddsub132_pd','8',''),
       ('VFMADDSUB213PD','fmaddsub213_pd','8',''),
       ('VFMADDSUB231PD','fmaddsub231_pd','8',''),
       ('VFMSUBADD132PS','fmaddsub132_ps','4','"1 |" + '),
       ('VFMSUBADD213PS','fmaddsub213_ps','4','"1 |" + '),
       ('VFMSUBADD231PS','fmaddsub231_ps','4','"1 |" + '),
       ('VFMSUBADD132PD','fmaddsub132_pd','8','"1 |" + '),
       ('VFMSUBADD213PD','fmaddsub213_pd','8','"1 |" + '),
       ('VFMSUBADD231PD','fmaddsub231_pd','8','"1 |" + ')]
list2=[('XMM','128','16'),('YMM','256','32'),('ZMM','512','64')]

for (instruction,func_name,elem_size,ext_arg) in list1:
    for (reg_type,size_bits,size_bytes) in list2:
        microcode += template_code % {"instruction": instruction,
                                      "func_name": func_name,
                                      "elem_size": elem_size,
                                      "reg_type": reg_type,
                                      "reg": reg_type.lower(),
                                      "size_bits": size_bits,
                                      "size_bytes": size_bytes,
                                      "ext_arg": ext_arg}
