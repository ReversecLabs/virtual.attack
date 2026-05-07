import { defineCollection } from 'astro:content';

const testCasesCollection = defineCollection({
  type: 'content',
});

export const collections = {
  'test-cases': testCasesCollection,
};
