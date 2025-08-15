/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // We create a custom sidebar for the main navigation
  mainSidebar: [
    'intro',
    'how-to-contribute',
    'glossary',
    {
      type: 'category',
      label: 'By Perspective',
      link: {
        type: 'doc',
        id: 'perspectives/index',
      },
      items: [
        'perspectives/eu-regulator',
        'perspectives/us-software-developer',
        'perspectives/global-sustainability-advocate',
      ],
    },
    {
      type: 'category',
      label: 'By Cluster',
      link: {
        type: 'generated-index',
        title: 'Thematic Clusters',
        description: 'The 51 questions are grouped into six thematic clusters for manageable review.',
        slug: '/clusters'
      },
      items: [
        'clusters/Ledger-Foundations-and-Accounting-Parallels/README',
        'clusters/Fidelity-Event-Theory-Auditability/README',
        'clusters/Assets-Liabilities-and-Metrics-in-ESG/README',
        'clusters/Subledgers-Process-Models-and-Supply-Chain/README',
        'clusters/Standards-Data-Flows-and-Confidentiality/README',
        'clusters/Controls-Anti-Greenwashing-and-Technology-Links/README',
      ],
    },
    {
      type: 'category',
      label: 'All Questions',
      link: {
        type: 'generated-index',
        title: 'All Questions',
        description: 'Browse all 51 questions.',
        slug: '/questions'
      },
      items: [
        'questions/Q1',
        'questions/Q2',
        'questions/Q3',
        'questions/Q4',
        'questions/Q5',
        'questions/Q6',
        'questions/Q7',
        'questions/Q8',
        'questions/Q9',
        'questions/Q10',
        'questions/Q11',
        'questions/Q12',
        'questions/Q13',
        'questions/Q14',
        'questions/Q15',
        'questions/Q16',
        'questions/Q17',
        'questions/Q18',
        'questions/Q19',
        'questions/Q20',
        'questions/Q21',
        'questions/Q22',
        'questions/Q23',
        'questions/Q24',
        'questions/Q25',
        'questions/Q26',
        'questions/Q27',
        'questions/Q28',
        'questions/Q29',
        'questions/Q30',
        'questions/Q31',
        'questions/Q32',
        'questions/Q33',
        'questions/Q34',
        'questions/Q35',
        'questions/Q36',
        'questions/Q37',
        'questions/Q38',
        'questions/Q39',
        'questions/Q40',
        'questions/Q41',
        'questions/Q42',
        'questions/Q43',
        'questions/Q44',
        'questions/Q45',
        'questions/Q46',
        'questions/Q47',
        'questions/Q48',
        'questions/Q49',
        'questions/Q50',
        'questions/Q51',
        'questions/Q52',
      ],
    },
    'all-in-one',
  ],
};

export default sidebars;