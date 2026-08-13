/**
 * ORM user-repository tests - BEFORE agent fix.
 * Scenario: repository returns real user objects; tests validate structure.
 */
const { UserRepository } = require('../src/user-repo');

describe('UserRepository', () => {
  it('returns full user object by id', async () => {
    const user = await UserRepository.findById('user-123');

    expect(user).toEqual({
      id: 'user-123',
      email: 'dev@example.com',
      role: 'admin',
      isActive: true,
    });
    expect(user.role).toBe('admin');
    expect(user.email).toMatch(/@example\.com$/);
  });

  it('returns list of users with expected schema', async () => {
    const users = await UserRepository.list({ limit: 3 });

    expect(users).toHaveLength(3);
    expect(users[0]).toMatchObject({ role: 'admin', isActive: true });
    expect(users.map((u) => u.email)).toContain('dev@example.com');
  });

  it('returns null when user does not exist', async () => {
    const user = await UserRepository.findById('missing-id');
    expect(user).toBe(null);
  });
});
