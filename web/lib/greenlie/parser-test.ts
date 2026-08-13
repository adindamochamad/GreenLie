import type { Assertion } from "./types";

type PolaAssertion = [RegExp, number, string];

// Urutan penting: first match wins per baris.
const POLA_JEST: PolaAssertion[] = [
  // Strict structural comparisons
  [/expect\s*\(.+?\)\s*\.toStrictEqual\s*\(/, 95, "strict_equal"],
  [/expect\s*\(.+?\)\s*\.toEqual\s*\(/, 85, "equal"],
  [/expect\s*\(.+?\)\s*\.toMatchObject\s*\(/, 82, "match_object"],
  // Exact literals
  [/expect\s*\(.+?\)\s*\.toBe\s*\(\s*['"][^'"]+['"]\s*\)/, 90, "exact_string"],
  [/expect\s*\(.+?\)\s*\.toBe\s*\(\s*\d+(?:\.\d+)?\s*\)/, 90, "exact_number"],
  [/expect\s*\(.+?\)\s*\.toBe\s*\(\s*true\s*\)/, 88, "exact_bool"],
  [/expect\s*\(.+?\)\s*\.toBe\s*\(\s*false\s*\)/, 88, "exact_bool"],
  [/expect\s*\(.+?\)\s*\.toBe\s*\(\s*null\s*\)/, 88, "exact_null"],
  // Exact identifier / dotted constant
  [
    /expect\s*\(.+?\)\s*\.toBe\s*\(\s*[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)+\s*\)/,
    82,
    "exact_dotted",
  ],
  [
    /expect\s*\(.+?\)\s*\.toBe\s*\(\s*[A-Za-z_$][\w$]*\s*\)/,
    80,
    "exact_identifier",
  ],
  // Specific matchers
  [/expect\s*\(.+?\)\s*\.toMatch\s*\(\s*\/[^/]+\/\s*\)/, 82, "regex_specific"],
  [/expect\s*\(.+?\)\s*\.toHaveLength\s*\(\s*\d+\s*\)/, 80, "length_exact"],
  [/expect\s*\(.+?\)\s*\.toContain\s*\(\s*['"][^'"]+['"]\s*\)/, 78, "contain_string"],
  [/expect\s*\(.+?\)\s*\.toContain\s*\(\s*\d+\s*\)/, 78, "contain_number"],
  // Exception matchers
  [
    /expect\s*\(.+?\)\s*\.toThrow\s*\(\s*['"][^'"]+['"]\s*\)/,
    88,
    "throws_message",
  ],
  [
    /expect\s*\(.+?\)\s*\.toThrow\s*\(\s*[A-Za-z_$][\w$.]*\s*\)/,
    85,
    "throws_specific",
  ],
  [/expect\s*\(.+?\)\s*\.toThrow\s*\(\s*\)/, 55, "throws_generic"],
  [/expect\s*\(.+?\)\s*\.toThrow\b/, 55, "throws_bare"],
  // Negated matchers
  [
    /expect\s*\(.+?\)\s*\.not\s*\.toBe\s*\(\s*(?:['"][^'"]*['"]|\d+|true|false|null|[A-Za-z_$][\w$.]*)\s*\)/,
    70,
    "not_exact",
  ],
  [/expect\s*\(.+?\)\s*\.not\s*\.toEqual\s*\(/, 70, "not_equal"],
  [/expect\s*\(.+?\)\s*\.not\s*\.toBeNull\s*\(\s*\)/, 75, "not_null"],
  [/expect\s*\(.+?\)\s*\.not\s*\.toBeUndefined\s*\(\s*\)/, 60, "not_undefined"],
  // Loose numeric ranges
  [/expect\s*\(.+?\)\s*\.toBeGreaterThanOrEqual\s*\(\s*\d+\s*\)/, 55, "range_gte"],
  [/expect\s*\(.+?\)\s*\.toBeLessThanOrEqual\s*\(\s*\d+\s*\)/, 55, "range_lte"],
  [/expect\s*\(.+?\)\s*\.toBeGreaterThan\s*\(\s*\d+\s*\)/, 50, "range_gt"],
  [/expect\s*\(.+?\)\s*\.toBeLessThan\s*\(\s*\d+\s*\)/, 50, "range_lt"],
  // Loosest matchers
  [/expect\s*\(.+?\)\s*\.toBeTruthy\s*\(\s*\)/, 35, "truthy"],
  [/expect\s*\(.+?\)\s*\.toBeFalsy\s*\(\s*\)/, 35, "falsy"],
  [/expect\s*\(.+?\)\s*\.toBeDefined\s*\(\s*\)/, 30, "defined"],
  [/expect\s*\(.+?\)\s*\.toBeUndefined\s*\(\s*\)/, 30, "undefined"],
  // Fallback generic toBe
  [/expect\s*\(.+?\)\s*\.toBe\s*\(/, 60, "to_be_generic"],
];

const POLA_PYTEST: PolaAssertion[] = [
  [/assert\s+[^#\n]+==\s*['"][^'"]+['"]/, 90, "assert_exact_string"],
  [/assert\s+[^#\n]+==\s*\d+(?:\.\d+)?/, 90, "assert_exact_number"],
  [/assert\s+[^#\n]+==\s*[A-Z][A-Za-z0-9_.]*/, 82, "assert_exact_constant"],
  [/assert\s+[^#\n]+\s+is\s+not\s+None/, 75, "assert_not_none"],
  [/assert\s+[^#\n]+\s+is\s+True/, 88, "assert_bool_true"],
  [/assert\s+[^#\n]+\s+is\s+False/, 88, "assert_bool_false"],
  [/pytest\.raises\s*\(\s*[A-Za-z_][\w.]*\s*\)/, 85, "raises_specific"],
  [/pytest\.raises\s*\(\s*\)/, 55, "raises_generic"],
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
