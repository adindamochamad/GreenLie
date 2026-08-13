/**
 * Payment validator tests - BEFORE agent fix.
 * Scenario: validator throws specific error types with specific messages.
 */
const { validatePayment } = require('../src/payment-validator');

describe('validatePayment', () => {
  it('throws ValidationError on missing currency', () => {
    expect(() => validatePayment({ amount: 100 })).toThrow(ValidationError);
  });

  it('throws with actionable message on negative amount', () => {
    expect(() => validatePayment({ amount: -1, currency: 'USD' })).toThrow('amount must be positive');
  });

  it('throws CurrencyNotSupportedError for unknown currency', () => {
    expect(() => validatePayment({ amount: 100, currency: 'XXX' })).toThrow(CurrencyNotSupportedError);
  });

  it('accepts valid payment', () => {
    const result = validatePayment({ amount: 100, currency: 'USD' });
    expect(result).toEqual({ ok: true, amount: 100, currency: 'USD' });
  });
});
