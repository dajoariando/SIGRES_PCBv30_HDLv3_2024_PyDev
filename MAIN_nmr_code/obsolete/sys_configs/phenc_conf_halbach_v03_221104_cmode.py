class phenc_conf_halbach_v03_221104_cmode():
# this configuration is for:
# halbach8 v02 that contains 30 turns rx solenoid coil, 1 turn gradient coils for x and z, 5 turns tx coil
    
    # precharging setting
    p90_pchg_us = 8.0
    p180_1st_pchg_us = 6.0
    p180_pchg_us = 2.0
    
    # cpmg settings
    cpmg_freq = 4.176 # in MHz
    bstrap_pchg_us = 2000
    lcs_pchg_us = 20
    lcs_dump_us = 100
    p90_us = 4.0 # 6.00, 10.00, 18.00, 24.00
    p90_dchg_us = p90_pchg_us # used to be 150
    p90_dtcl = 0.5
    p180_us = p90_us
    p180_dchg_us = p180_pchg_us # used to be p90_dchg_us
    p180_dtcl = p90_dtcl
    echoshift_us = 5
    echotime_us = 25# 400
    scanspacing_us = 400000
    samples_per_echo = 160 # 300
    echoes_per_scan = 60 # 80
    n_iterate =  2
    ph_cycl_en = 1 # phase cycle enable
    dconv_fact = 1 # unused for current cpmg code
    echoskip = 1 # unused for current cpmg code
    echodrop = 0 # unused for current cpmg code
    vvarac = -1.8 # set to -1.91V # more negative, more capacitance
    # precharging the vpc
    lcs_vpc_pchg_us = 25
    lcs_recycledump_us = 1000
    lcs_vpc_pchg_repeat = 210
    # discharging the vpc
    lcs_vpc_dchg_us = 5
    lcs_wastedump_us = 200
    lcs_vpc_dchg_repeat = 2000
    # gradient params
    gradz_len_us = 100 # gradient pulse length
    gradz_volt = 0.1 # the gradient can be positive or negative
    gradx_len_us = 100 # gradient pulse length
    gradx_volt = 0.1 # the gradient can be positive or negative
    grad_refocus = 1 # put 1 to refocus the gradient
    flip_grad_refocus_sign = 1 # put 1 to flip the gradient refocusing sign
    enc_tao_us = 200 # the encoding time
    # p180 x-y pulse selection. 
    # p180_xy_angle = 2 # set 1 for x-pulse and 2 for y-pulse for p180
    # lcs charging param
    en_lcs_pchg = 1 # enable lcs precharging
    en_lcs_dchg = 1 # enable lcs discharging
    
    # post-processing parameters
    dconv_f = 0 # in MHz. when set to 0, the downconversion local oscillator is set to be B1 freq. When set the other value, the downconversion losc is just the set value.
    dconv_lpf_ord = 2  # downconversion order
    dconv_lpf_cutoff_kHz = 200  # downconversion lpf cutoff
    en_ext_rotation = 0 # enable external reference for echo rotation
    thetaref = 0 # external parameter: echo rotation angle
    en_ext_matchfilter = 0 # enable external reference for matched filtering
    en_conj_matchfilter = 0 # compute matchfiltering with the conjugate (results in absolute value of signal with no imaginary)
    en_self_rotation = 1 # enable self rotation with the angle estimated by its own echo (is automatically disactivated when en_ext_rotation is active
    echoref_avg = 0 # echo_avg_ref # external parameter: matched filtering echo average 
    ignore_echoes = 0 # ignore initial echoes for data processing
    # dual_exp = 0 # enable dual exponential fit. Otherwise, it will be single exponential fit
    a_est = [200,10] # amplitude estimation for fitting
    t2_est = [1e-3,0.1e-3] # t2 estimate for fitting
    #a_est = [200] # array of amplitude estimate for fitting
    #t2_est = [1e-3] # array of t2 estimate for fitting
    
