import type { Assertion } from "./types";

type PolaAssertion = [RegExp, number, string];

const POLA_JEST: PolaAssertion[] = [
  [/expect\s*\([^)]+\)\s*\.toStrictEqual\s*\(/, 95, "strict_equal"],
  [/expect\s*\([^)]+\)\s*\.toEqual\s*\(/, 85, "equal"],
  [/expect\s*\([^)]+\)\s*\.toBe\s*\(\s*['"][^'"]+['"]\s*\)/, 90, "exact_string"],
  [/expect\s*\([^)]+\)\s*\.toBe\s*\(\s*\d+\s*\)/, 90, "exact_number"],
  [/expect\s*\([^)]+\)\s*\.toBe\s*\(\s*true\s*\)/, 88, "exact_bool"],
  [/expect\s*\([^)]+\)\s*\.toBe\s*\(\s*false\s*\)/, 88, "exact_bool"],
  [/expect\s*\([^)]+\)\s*\.toMatch\s*\(\s*\/[^/]+\/\s*\)/, 82, "regex_specific"],
  [/expect\s*\([^)]+\)\s*\.toHaveLength\s*\(\s*\d+\s*\)/, 80, "length_exact"],
  [/expect\s*\([^)]+\)\s*\.toThrow\s*\(/, 85, "throws"],
  [/expect\s*\([^)]+\)\s*\.toBeGreaterThanOrEqual\s*\(\s*\d+\s*\)/, 55, "range_gte"],
  [/expect\s*\([^)]+\)\s*\.toBeGreaterThan\s*\(\s*\d+\s*\)/, 50, "range_gt"],
  [/expect\s*\([^)]+\)\s*\.toBeLessThan\s*\(\s*\d+\s*\)/, 50, "range_lt"],
  [/expect\s*\([^)]+\)\s*\.toBeTruthy\s*\(\s*\)/, 35, "truthy"],
  [/expect\s*\([^)]+\)\s*\.toBeDefined\s*\(\s*\)/, 30, "defined"],
  [/expect\s*\([^)]+\)\s*\.not\s*\.toBeNull\s*\(\s*\)/, 75, "not_null"],
];

const POLA_PYTEST: PolaAssertion[] = [
  [/assert\s+[^#\n]+==\s*['"][^'"]+['"]/, 90, "assert_exact_string"],
  [/assert\s+[^#\n]+==\s*\d+/, 90, "assert_exact_number"],
  [/assert\s+[^#\n]+\s+is\s+not\s+None/, 75, "assert_not_none"],
  [/assert\s+[^#\n]+\s+is\s+True/, 88, "assert_bool"],
  [/assert\s+[^#\n]+\s+is\s+False/, 88, "assert_bool"],
  [/pytest\.raises\s*\(/, 85, "raises"],
  [/assert\s+[^#\n]+/, 60, "assert_loose"],
];

export function apakahBerkasTest(namaBerkas: string, namaFolderInduk: string): boolean {
  const nama = namaBerkas.toLowerCase();
  if (nama.startsWith("test_") && nama.endsWith(".py")) return true;
  if (nama.includes(".test.") || nama.includes(".spec.")) return true;
  if (nama.endsWith("_test.py")) return true;
  return ["tests", "__tests__", "test"].includes(namaFolderInduk);
}

export function ekstrakAssertion(isi: string, ekstensiBerkas: string): Assertion[] {
  const polaList = ekstensiBerkas === ".py" ? POLA_PYTEST : POLA_JEST;
  const barisList = isi.split("\n");
  const hasil: Assertion[] = [];

  for (let indeks = 0; indeks < barisList.length; indeks++) {
    const barisBersih = barisList[indeks].trim();
    if (!barisBersih || barisBersih.startsWith("//") || barisBersih.startsWith("#")) {
      continue;
    }

    for (const [pola, ketat, jenis] of polaList) {
      if (pola.test(barisBersih)) {
        hasil.push({
          teks: barisBersih,
          baris: indeks + 1,
          tingkat_ketat: ketat,
          jenis,
        });
        break;
      }
    }
  }

  return hasil;
}
