from pkg_py.pk_core import save_power_as_s4, pk_speak, save_screen

save_screen()

pk_speak('최대 절전 모드 진입', after_delay=0.55)
save_power_as_s4()
# make_os_power_saving_mode_as_s3()
