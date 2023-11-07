def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    mnum = int(input('Enter the number of male students: '))
    fnum = int(input('Enter the number of female students: '))


    total = mnum + fnum
    m_perc = mnum / total * 100
    f_perc = fnum / total * 100
    print(f'Percentage of male students: {m_perc:.2f}')
    print(f'Percentage of female students: {f_perc:.2f}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
