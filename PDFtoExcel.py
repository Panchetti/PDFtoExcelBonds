import pdfplumber
import pandas as pd


def parse_bond_data(text):
    lines = text.split('\n')
    bonds = []
    for line in lines:
        if "/" in line and "page" not in line and 'Isin' not in line:
            parts = line.split(" ")
            print(parts)
            if "l" not in parts:
                if "(wl-)" not in parts and '(wl+)' not in parts:
                    try:

                        parts = line.split()

                        Isin = parts[0]
                        currency = parts[1]
                        cpn = parts[2]
                        issuer = " ".join(parts[3:parts.index('/') - 10])
                        maturity = parts[parts.index('/') - 10]

                        AmntOut = " ".join(parts[parts.index('/') - 9:parts.index('/') - 7])
                        Ask = parts[parts.index('/') - 7]
                        Yield = parts[parts.index('/') - 6]
                        DSwap = parts[parts.index('/') - 5]
                        Dur = parts[parts.index('/') - 4]

                        Pieces = parts[parts.index('/') - 3]

                        Rating = parts[parts.index('/') - 2]
                        if parts[parts.index('/') + 1] =='Real':
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') +3])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 3:])
                            except IndexError:
                                Misc = ""
                        else:
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 2])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 2:])
                            except IndexError:
                                Misc = ""

                        bonds.append([Isin, currency, cpn, issuer, maturity, AmntOut, Ask, Yield, DSwap, Dur, Pieces, Rating,
                                     City, Misc])

                    except Exception as e:
                        print(f"Error parsing line: {line}")
                        print(f"Error: {e}")
                        continue
                else:

                    try:
                        parts = line.split()

                        Isin = parts[0]
                        currency = parts[1]
                        cpn = parts[2]
                        issuer = " ".join(parts[3:parts.index('/') - 11])
                        maturity = parts[parts.index('/') - 11]

                        AmntOut = " ".join(parts[parts.index('/') - 10:parts.index('/') - 8])
                        Ask = parts[parts.index('/') - 8]
                        Yield = parts[parts.index('/') - 7]
                        DSwap = parts[parts.index('/') - 6]
                        Dur = parts[parts.index('/') - 5]

                        Pieces = parts[parts.index('/') - 4]

                        Rating = " ".join(parts[parts.index('/') - 3:parts.index('/') - 1])

                        if parts[parts.index('/') + 1] == 'Real':
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 3])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 3:])
                            except IndexError:
                                Misc = ""
                        else:
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 2])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 2:])
                            except IndexError:
                                Misc = ""
                        bonds.append(
                            [Isin, currency, cpn, issuer, maturity, AmntOut, Ask, Yield, DSwap, Dur, Pieces, Rating,
                             City, Misc])

                    except Exception as e:
                        print(f"Error parsing line: {line}")
                        print(f"Error: {e}")
                        continue

            else:
                if "(wl-)" not in parts and '(wl+)' not in parts:
                    try:

                        parts = line.split()

                        Isin = parts[0]
                        currency = parts[1]
                        cpn = parts[2]
                        issuer = " ".join(parts[3:parts.index('/') - 11])
                        maturity = parts[parts.index('/') - 11]

                        AmntOut = " ".join(parts[parts.index('/') - 10:parts.index('/') - 8])
                        Ask = parts[parts.index('/') - 8]
                        Yield = parts[parts.index('/') - 7]
                        DSwap = parts[parts.index('/') - 6]
                        Dur = parts[parts.index('/') - 5]

                        Pieces = parts[parts.index('/') - 4]
                        Rating = parts[parts.index('/') - 2]
                        if parts[parts.index('/') + 1] == 'Real':
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 3])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 3:])
                            except IndexError:
                                Misc = ""
                        else:
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 2])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 2:])
                            except IndexError:
                                Misc = ""
                        bonds.append(
                            [Isin, currency, cpn, issuer, maturity, AmntOut, Ask, Yield, DSwap, Dur, Pieces, Rating,
                             City, Misc])

                    except Exception as e:
                        print(f"Error parsing line: {line}")
                        print(f"Error: {e}")
                        continue
                else:
                    try:

                        parts = line.split()

                        Isin = parts[0]
                        currency = parts[1]
                        cpn = parts[2]
                        issuer = " ".join(parts[3:parts.index('/') - 12])
                        maturity = parts[parts.index('/') - 12]

                        AmntOut = " ".join(parts[parts.index('/') - 11:parts.index('/') - 9])
                        Ask = parts[parts.index('/') - 9]
                        Yield = parts[parts.index('/') - 8]
                        DSwap = parts[parts.index('/') - 7]
                        Dur = parts[parts.index('/') - 6]

                        Pieces = parts[parts.index('/') - 5]
                        Rating = "".join(parts[parts.index('/') - 3:parts.index('/') - 1])
                        if parts[parts.index('/') + 1] == 'Real':
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 3])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 3:])
                            except IndexError:
                                Misc = ""
                        else:
                            City = " ".join(parts[parts.index('/') - 1:parts.index('/') + 2])
                            try:

                                Misc = " ".join(parts[parts.index('/') + 2:])
                            except IndexError:
                                Misc = ""
                        bonds.append(
                            [Isin, currency, cpn, issuer, maturity, AmntOut, Ask, Yield, DSwap, Dur, Pieces, Rating,
                             City, Misc])

                    except Exception as e:
                        print(f"Error parsing line: {line}")
                        print(f"Error: {e}")
                        continue

    return bonds


# Open the PDF file
pdf_path = ''
with pdfplumber.open(pdf_path) as pdf:
    text = ''
    for page in pdf.pages[2:len(pdf.pages) - 1]:
        page_text = page.extract_text()
        if page_text:  # Check if text is extracted
            text += page_text
        else:
            print(f"Warning: No text extracted from page {page.page_number}")

# Parse the bond data
bond_data = parse_bond_data(text)


# Create a DataFrame
columns = ['Isin', 'currency', 'cpn', 'issuer', 'maturity', 'AmntOut', 'Ask', 'Yield', 'DSwap', 'Dur', 'Pieces',
           'Rating', 'CitySec', 'Misc']
df = pd.DataFrame(bond_data, columns=columns)

# Check if DataFrame is created correctly
print(df.head())

# Save to Excel
output_path = ''
df.to_excel(output_path, index=False, sheet_name='Sheet1')

print(f"Bond data has been saved to {output_path}")
