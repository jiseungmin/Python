# import theater_module *   theater_module 파일의 함수를 가져올수있음 *는 모든것을 쓸수 있음.
# theater_module.price(3)
# theater_module.monning_price(3)
# theater_module.solider_price(3)


# import theater_module as mb   # mb로 초기화 시켜서 쓸수 있음.
# mb.price(3)
# mb.monning_price(3)
# mb.solider_price(3)


from theater_module import price, monning_price
price(3)
monning_price(3)
