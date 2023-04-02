from typing import Union


def calculate_tax_and_remain_mainland(input: Union[int, float]) -> tuple[float, float]:
    if input <= 36000:
        tax = input * 0.03
    elif input > 36000 and input <= 144000:
        tax = 36000 * 0.03 + (input - 36000) * 0.1
    elif input > 144000 and input <= 300000:
        tax = 36000 * 0.03 + (144000 - 36000) * 0.1 + (input - 144000) * 0.2
    elif input > 300000 and input <= 420000:
        tax = 36000 * 0.03 + (144000 - 36000) * 0.1 + (300000 - 144000) * 0.2 + (input - 300000) * 0.25
    elif input > 420000 and input <= 600000:
        tax = 36000 * 0.03 + (144000 - 36000) * 0.1 + (300000 - 144000) * 0.2 + (420000 - 300000) * 0.25 + (input - 420000) * 0.3
    elif input > 600000 and input <= 960000:
        tax = 36000 * 0.03 + (144000 - 36000) * 0.1 + (300000 - 144000) * 0.2 + (420000 - 300000) * 0.25 + (600000 - 420000) * 0.3 + (input - 600000) * 0.35
    else:
        tax = 36000 * 0.03 + (144000 - 36000) * 0.1 + (300000 - 144000) * 0.2 + (420000 - 300000) * 0.25 + (600000 - 420000) * 0.3 + (960000 - 600000) * 0.35 + (input - 960000) * 0.45
    return tax, input - tax


def calculate_tax_and_remain_hengqin(input: Union[int, float]) -> tuple[float, float]:
    # 根据 2022 年的政策，珠海横琴个人所得税超过 15% 的部分免征。
    if input <= 36000:
        tax = input * 0.03
    elif input > 36000 and input <= 144000:
        tax = 36000 * 0.03 + (input - 36000) * 0.1
    else:
        tax = 36000 * 0.03 + (144000 - 36000) * 0.1 + (input - 144000) * 0.15
    return tax, input - tax


def calculate_tax_and_remain_macao(input: Union[int, float]) -> tuple[float, float]:
    # 根据澳门 2023 年度全年职业税计算公式
    if input <= 144000:
        tax = 0
    elif input > 144000 and input <= 164000:
        tax = (input - 144000) * 0.07
    elif input > 164000 and input <= 184000:
        tax = (164000 - 144000) * 0.07 + (input - 164000) * 0.08
    elif input > 184000 and input <= 224000:
        tax = (164000 - 144000) * 0.07 + (184000 - 164000) * 0.08 + (input - 184000) * 0.09
    elif input > 224000 and input <= 304000:
        tax = (164000 - 144000) * 0.07 + (184000 - 164000) * 0.08 + (224000 - 184000) * 0.09 + (input - 224000) * 0.1
    elif input > 304000 and input <= 424000:
        tax = (164000 - 144000) * 0.07 + (184000 - 164000) * 0.08 + (224000 - 184000) * 0.09 + (304000 - 224000) * 0.1 + (input - 304000) * 0.11
    else:
        tax = (164000 - 144000) * 0.07 + (184000 - 164000) * 0.08 + (224000 - 184000) * 0.09 + (304000 - 224000) * 0.1 + (424000 - 304000) * 0.11 + (input - 424000) * 0.12
    return tax, input - tax


def main() -> None:
    pkg = int(input("请输入全年应纳税所得额："))
    tax, remain = calculate_tax_and_remain_mainland(pkg)
    print(f"内地应缴税额：{ tax }")
    print(f"内地实际到手：{ remain }")
    tax, remain = calculate_tax_and_remain_hengqin(pkg)
    print(f"珠海横琴应缴税额：{ tax }")
    print(f"珠海横琴实际到手：{ remain }")
    tax, remain = calculate_tax_and_remain_macao(pkg)
    print(f"澳门应缴税额：{ tax }")
    print(f"澳门实际到手：{ remain }")


if __name__ == '__main__':
    main()