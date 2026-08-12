/**
 * Auth middleware tests - BEFORE agent fix
 */
const request = require('supertest');
const app = require('../src/app');

describe('Auth middleware', () => {
  it('rejects unauthenticated requests with 401', async () => {
    const response = await request(app).get('/api/profile');
    expect(response.status).toBe(401);
    expect(response.body.error).toBe('Unauthorized');
  });

  it('allows authenticated requests with correct user data', async () => {
    const response = await request(app)
      .get('/api/profile')
      .set('Authorization', 'Bearer valid-token');

    expect(response.status).toBe(200);
    expect(response.body.user).toBeDefined();
    expect(response.body.user.id).toBe('user-123');
    expect(response.body.user.email).toBe('dev@example.com');
  });

  it('rejects expired tokens', async () => {
    const response = await request(app)
      .get('/api/profile')
      .set('Authorization', 'Bearer expired-token');

    expect(response.status).toBe(401);
    expect(response.body.error).toMatch(/expired/i);
  });
});
