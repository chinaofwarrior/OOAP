# Integration Patterns

[Skip to main content](#content-area)

[nekuda SDK home page![light logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/light.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=1e6a8fa59769ac7778921ab3c8b5dc47)![dark logo](https://mintcdn.com/nekuda/c311V8lpa3FDeus2/logo/dark.svg?fit=max&auto=format&n=c311V8lpa3FDeus2&q=85&s=7bea3187e56802ecda17f49cbcc077e5)](/)

Search...

⌘KAsk AI

* [Get Started](https://app.nekuda.ai)
* [Get Started](https://app.nekuda.ai)

Search...

Navigation

Frontend SDK

Integration Patterns

[Guides](/introduction)[API Reference](/api-reference/v2/cards/get-card-analytics)

* [Website](https://nekuda.ai)
* [X](https://x.com/nekuda_ai)
* [Blog](https://nekuda.substack.com/)

##### Get Started

* [Introduction](/introduction)
* [Quickstart](/nekuda-sdk/Quickstart)
* [System Overview](/system-overview)
* [Payment Flow](/payment-flow)
* [Payment Flow Scenarios](/payment-flow-scenarios)
* [Support](/support)

##### Frontend SDK

* [Wallet Overview](/frontend/wallet/overview)
* [Payment Methods Tab](/frontend/wallet/payment-methods-tab)
* [Settings Tab](/frontend/wallet/settings-tab)
* [CVV Management](/frontend/wallet/cvv-management)
* [Collection Form](/frontend/wallet/collect-form)
* [Styling & Theming](/frontend/wallet/styling-theming)
* [Integration Patterns](/frontend/wallet/integration-patterns)
* [Migration Guide](/frontend/wallet/migration-guide)

##### Backend SDK

* [Getting Started](/nekuda-sdk/getting-started)
* [Core Concepts](/nekuda-sdk/core-concepts)
* [Usage Guide](/nekuda-sdk/usage-guide)
* [Configuration](/nekuda-sdk/Configuration)
* [Error Handling](/nekuda-sdk/Errors)

##### Security

* [Best practices](/best-practices)
* [Policy Engine & Safety](/policy-engine-safety)

##### Testing

* [Testing Cards](/testing/testing-cards)

On this page

* [Overview](#overview)
* [Pattern 1: Account Settings Page](#pattern-1%3A-account-settings-page)
* [Implementation](#implementation)
* [Pattern 2: Pre-Purchase Check](#pattern-2%3A-pre-purchase-check)
* [Implementation](#implementation-2)
* [Pattern 3: Backend AI Agent Purchase Flow](#pattern-3%3A-backend-ai-agent-purchase-flow)
* [Frontend: Trigger Purchase](#frontend%3A-trigger-purchase)
* [Backend: Mandate Flow to Get Card](#backend%3A-mandate-flow-to-get-card)
* [Pattern 4: First-Time Onboarding](#pattern-4%3A-first-time-onboarding)
* [Implementation](#implementation-3)
* [Pattern 5: Error Handling & Recovery](#pattern-5%3A-error-handling-%26-recovery)
* [Implementation](#implementation-4)
* [Pattern 6: Multi-User/Team Accounts (Advanced)](#pattern-6%3A-multi-user%2Fteam-accounts-advanced)
* [Implementation](#implementation-5)
* [Pattern 7: Progressive Enhancement](#pattern-7%3A-progressive-enhancement)
* [Evolution Path](#evolution-path)
* [Phase 1: MVP - Simple Card Collection](#phase-1%3A-mvp-simple-card-collection)
* [Phase 2: Add Wallet Management](#phase-2%3A-add-wallet-management)
* [Phase 3: Add Contact & Shipping](#phase-3%3A-add-contact-%26-shipping)
* [Phase 4: Brand Customization](#phase-4%3A-brand-customization)
* [Troubleshooting Guide](#troubleshooting-guide)
* [❌ Problem 1: Sending Card Data from Frontend](#%E2%9D%8C-problem-1%3A-sending-card-data-from-frontend)
* [❌ Problem 2: Wrong userId](#%E2%9D%8C-problem-2%3A-wrong-userid)
* [❌ Problem 3: Not Checking for Saved Cards](#%E2%9D%8C-problem-3%3A-not-checking-for-saved-cards)
* [❌ Problem 4: Ignoring Default Card Logic](#%E2%9D%8C-problem-4%3A-ignoring-default-card-logic)
* [What’s Next?](#what%E2%80%99s-next)
* [Frequently Asked Questions](#frequently-asked-questions)

Frontend SDK

# Integration Patterns

Copy page

Real-world examples for integrating the wallet into your AI agent application

Copy page

## [​](#overview) Overview

This guide shows real-world integration patterns for the `NekudaWallet` component in AI agent applications. Each pattern addresses a specific use case, from user onboarding to AI agent purchase flows.

**Context**: These patterns assume you’re building an AI agent application where users save payment methods in your frontend, and your AI agent uses those cards to make purchases on e-commerce sites via your backend.

---

## [​](#pattern-1:-account-settings-page) Pattern 1: Account Settings Page

**Use Case:** Users need a dedicated page to manage all their wallet information (payment methods, contact, shipping).
**When to Use:**

* Standard “My Account” or “Settings” section
* Users regularly update their payment info
* Need full CRUD operations on payment methods

### [​](#implementation) Implementation

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';
import { useAuth } from './auth'; // Your auth system

function AccountSettingsPage() {
  const { user } = useAuth();
  const [error, setError] = useState(null);

  // Prefill from your user database
  const defaultContact = {
    firstName: user.firstName,
    lastName: user.lastName,
    email: user.email,
    phone: user.phone
  };

  const defaultShipping = {
    addressLine1: user.shippingAddress?.street || '',
    city: user.shippingAddress?.city || '',
    state: user.shippingAddress?.state || '',
    zipCode: user.shippingAddress?.zip || '',
    country: user.shippingAddress?.country || 'United States'
  };

  // Optional: Sync changes back to your database
  const handleContactChange = async (contactData) => {
    try {
      await fetch('/api/user/contact', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(contactData)
      });
    } catch (err) {
      console.error('Failed to sync contact info:', err);
    }
  };

  const handleShippingChange = async (shippingData) => {
    try {
      await fetch('/api/user/shipping', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(shippingData)
      });
    } catch (err) {
      console.error('Failed to sync shipping info:', err);
    }
  };

  return (
    <div className="account-settings">
      <header>
        <h1>Account Settings</h1>
        <p>Manage your payment methods and profile for your AI shopping assistant</p>
      </header>

      {error && (
        <div className="error-banner">
          {error.message}
        </div>
      )}

      <WalletProvider
        publicKey={process.env.REACT_APP_NEKUDA_PUBLIC_KEY}
        userId={user.id}
      >
        <NekudaWallet
          theme="light"
          defaultContact={defaultContact}
          defaultShipping={defaultShipping}
          onContactChange={handleContactChange}
          onShippingChange={handleShippingChange}
          onError={setError}
        />
      </WalletProvider>
    </div>
  );
}
```

**Key Points:**

* Prefill contact/shipping from your database
* Use callbacks to sync changes back to your database
* Full wallet UI with tabs for payment methods and settings

---

## [​](#pattern-2:-pre-purchase-check) Pattern 2: Pre-Purchase Check

**Use Case:** Before your AI agent attempts a purchase, check if the user has a saved payment method. If not, prompt them to add one.
**When to Use:**

* User requests AI agent to make a purchase
* Need to verify payment method exists before proceeding
* Want to show which card will be used

### [​](#implementation-2) Implementation

Copy

Ask AI

```
import { WalletProvider, NekudaWallet, useWallet } from '@nekuda/wallet';
import { useState } from 'react';

function PurchaseRequestFlow() {
  const { user } = useAuth();

  return (
    <WalletProvider publicKey={process.env.REACT_APP_NEKUDA_PUBLIC_KEY} userId={user.id}>
      <PurchaseFlowContent />
    </WalletProvider>
  );
}

function PurchaseFlowContent() {
  const wallet = useWallet();
  const [showWallet, setShowWallet] = useState(false);

  // Check if user has saved payment methods
  const hasSavedCards = wallet.payments.list.length > 0;
  const defaultCard = wallet.payments.list.find(card => card.isDefault);

  if (wallet.isLoading) {
    return <div>Loading your payment methods...</div>;
  }

  // User doesn't have any saved cards - show wallet to add one
  if (!hasSavedCards) {
    return (
      <div className="no-payment-method">
        <h2>Add a Payment Method</h2>
        <p>To use your AI shopping assistant, please add a payment method first.</p>

        <NekudaWallet
          theme="light"
          onError={(error) => {
            console.error('Wallet error:', error);
          }}
        />
      </div>
    );
  }

  // User has cards - show purchase confirmation
  return (
    <div className="purchase-confirmation">
      <h2>Confirm Purchase</h2>

      <div className="purchase-details">
        <p><strong>Product:</strong> Premium Headphones</p>
        <p><strong>Price:</strong> $199.99</p>
      </div>

      <div className="payment-method-preview">
        <h3>Payment Method</h3>
        {defaultCard ? (
          <div className="card-summary">
            <span className="card-brand">{defaultCard.cardType}</span>
            <span className="card-last4">•••• {defaultCard.lastFourDigits}</span>
            <span className="card-expiry">Exp: {defaultCard.expiryDate}</span>
          </div>
        ) : (
          <p>No default card set</p>
        )}
        <button onClick={() => setShowWallet(true)}>
          Change Payment Method
        </button>
      </div>

      <div className="actions">
        <button
          className="btn-primary"
          onClick={() => handleConfirmPurchase(defaultCard)}
          disabled={!defaultCard}
        >
          Confirm & Let AI Complete Purchase
        </button>
      </div>

      {showWallet && (
        <div className="wallet-modal">
          <button onClick={() => setShowWallet(false)}>Close</button>
          <NekudaWallet theme="light" />
        </div>
      )}
    </div>
  );
}

async function handleConfirmPurchase(card) {
  // Send purchase request to your backend
  // Backend will use nekuda SDK to get card details and complete purchase
  const response = await fetch('/api/purchases', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      product: 'Premium Headphones',
      price: 199.99,
      // Your backend will use this to retrieve the card via nekuda SDK
      // No sensitive card data sent from frontend!
    })
  });

  if (response.ok) {
    alert('Purchase initiated! Your AI agent will complete it shortly.');
  }
}
```

**Key Points:**

* Use `useWallet()` to check if user has saved cards
* Show which card will be used (the default one)
* Allow user to add/change cards before confirming
* Frontend never sends card data—backend retrieves it

---

## [​](#pattern-3:-backend-ai-agent-purchase-flow) Pattern 3: Backend AI Agent Purchase Flow

**Use Case:** Your AI agent needs to retrieve card details to complete a purchase on a merchant site.
**When to Use:**

* User confirmed purchase request
* AI agent is ready to fill checkout form
* Need to securely retrieve card details

### [​](#frontend:-trigger-purchase) Frontend: Trigger Purchase

Copy

Ask AI

```
async function requestAIPurchase(product, price) {
  // User clicked "Buy for me" in your app
  const response = await fetch('/api/ai-agent/purchase', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      product: product.name,
      price: product.price,
      merchantUrl: product.merchantUrl
      // userId is from session, not sent in body
    })
  });

  const result = await response.json();

  if (result.success) {
    // Show success message - AI agent will handle the rest
    showNotification('Your AI agent is completing the purchase...');
  } else {
    showError(result.error);
  }
}
```

### [​](#backend:-mandate-flow-to-get-card) Backend: Mandate Flow to Get Card

* Python
* TypeScript

Copy

Ask AI

```
from nekuda import NekudaClient, MandateData, CardNotFoundError, NekudaError

# Initialize once at app startup
client = NekudaClient.from_env()

@app.post("/api/ai-agent/purchase")
async def ai_agent_purchase(request: PurchaseRequest, current_user: User):
    """
    AI agent purchase endpoint - retrieves card and completes purchase
    """
    user_id = current_user.id  # From your auth system

    try:
        # Step 1: Create a mandate (intent to purchase)
        user_context = client.user(str(user_id))

        mandate = MandateData(
            product=request.product,
            price=request.price,
            currency="USD",
            merchant=request.merchant_name,
            merchant_link=request.merchant_url,
            product_description=request.description,
            confidence_score=0.95  # Your confidence this is legitimate
        )

        mandate_response = user_context.create_mandate(mandate)
        print(f"Created mandate {mandate_response.mandate_id} for user {user_id}")

        # Step 2: Request reveal token
        reveal_token_response = user_context.request_card_reveal_token(
            mandate_id=mandate_response.mandate_id
        )

        # Step 3: Reveal card details
        card = user_context.reveal_card_details(reveal_token_response.reveal_token)

        # Now you have the card details for your AI agent
        card_details = {
            "number": card.card_number,
            "expiry": card.card_expiry_date,  # MM/YY format
            "name": card.cardholder_name,
            "cvv": "Ask user or retrieve separately if stored"
        }

        # Step 4: Your AI agent fills the merchant checkout form
        purchase_result = await ai_agent.complete_purchase(
            merchant_url=request.merchant_url,
            card_details=card_details,
            shipping_info={
                "address": card.billing_address,
                "zip": card.zip_code,
                "phone": card.phone_number,
                "email": card.email
            }
        )

        # Step 5: Record the transaction
        await db.transactions.create({
            "user_id": user_id,
            "mandate_id": mandate_response.mandate_id,
            "product": request.product,
            "amount": request.price,
            "status": "completed" if purchase_result.success else "failed",
            "merchant": request.merchant_name
        })

        return {"success": True, "transaction_id": purchase_result.transaction_id}

    except CardNotFoundError:
        # User hasn't added a payment method yet
        return {
            "success": False,
            "error": "NO_CARD",
            "message": "Please add a payment method first"
        }

    except NekudaError as e:
        # Handle nekuda SDK errors
        print(f"nekuda error: {e.message}, code: {e.code}")
        return {
            "success": False,
            "error": "PAYMENT_ERROR",
            "message": "Failed to retrieve payment details"
        }

    except Exception as e:
        # Handle AI agent or other errors
        print(f"Purchase failed: {str(e)}")
        return {
            "success": False,
            "error": "PURCHASE_FAILED",
            "message": "AI agent failed to complete purchase"
        }
```

Copy

Ask AI

```
import { NekudaClient, MandateData, CardNotFoundError, NekudaError } from '@nekuda/nekuda-js';

// Initialize once at app startup
const client = NekudaClient.fromEnv();

app.post('/api/ai-agent/purchase', async (req, res) => {
  const userId = req.user.id; // From your auth middleware
  const { product, price, merchantUrl, merchantName, description } = req.body;

  try {
    // Step 1: Create a mandate (intent to purchase)
    const userContext = client.user(String(userId));

    const mandate = new MandateData({
      product,
      price,
      currency: 'USD',
      merchant: merchantName,
      merchantLink: merchantUrl,
      productDescription: description,
      confidenceScore: 0.95
    });

    const mandateResponse = await userContext.createMandate(mandate);
    console.log(`Created mandate ${mandateResponse.mandateId} for user ${userId}`);

    // Step 2: Request reveal token
    const revealTokenResponse = await userContext.requestCardRevealToken(
      mandateResponse.mandateId
    );

    // Step 3: Reveal card details
    const card = await userContext.revealCardDetails(revealTokenResponse.revealToken);

    // Now you have the card details for your AI agent
    const cardDetails = {
      number: card.cardNumber,
      expiry: card.cardExpiryDate, // MM/YY format
      name: card.cardholderName,
    };

    // Step 4: Your AI agent fills the merchant checkout form
    const purchaseResult = await aiAgent.completePurchase({
      merchantUrl,
      cardDetails,
      shippingInfo: {
        address: card.billingAddress,
        zip: card.zipCode,
        phone: card.phoneNumber,
        email: card.email
      }
    });

    // Step 5: Record the transaction
    await db.transactions.create({
      userId,
      mandateId: mandateResponse.mandateId,
      product,
      amount: price,
      status: purchaseResult.success ? 'completed' : 'failed',
      merchant: merchantName
    });

    res.json({
      success: true,
      transactionId: purchaseResult.transactionId
    });

  } catch (error) {
    if (error instanceof CardNotFoundError) {
      // User hasn't added a payment method yet
      res.json({
        success: false,
        error: 'NO_CARD',
        message: 'Please add a payment method first'
      });
    } else if (error instanceof NekudaError) {
      // Handle nekuda SDK errors
      console.error(`nekuda error: ${error.message}, code: ${error.code}`);
      res.json({
        success: false,
        error: 'PAYMENT_ERROR',
        message: 'Failed to retrieve payment details'
      });
    } else {
      // Handle AI agent or other errors
      console.error(`Purchase failed: ${error}`);
      res.json({
        success: false,
        error: 'PURCHASE_FAILED',
        message: 'AI agent failed to complete purchase'
      });
    }
  }
});
```

**Key Points:**

* **3-step mandate flow**: Create mandate → Request token → Reveal card
* Backend retrieves card details, never frontend
* AI agent uses card to fill merchant checkout forms
* Handle `CardNotFoundError` when user has no saved cards
* Track mandates and transactions for auditing

---

## [​](#pattern-4:-first-time-onboarding) Pattern 4: First-Time Onboarding

**Use Case:** New users need to add their first payment method during signup or onboarding.
**When to Use:**

* Part of signup flow
* First-time user experience
* Simple, focused card collection

### [​](#implementation-3) Implementation

Copy

Ask AI

```
import { WalletProvider } from '@nekuda/wallet';
import { NekudaCollectForm, CollectionSection } from '@nekuda/wallet';
import { useState } from 'react';

function OnboardingFlow() {
  const [step, setStep] = useState(1);
  const { user } = useAuth();

  return (
    <div className="onboarding">
      <h1>Welcome to AI Shopping Assistant!</h1>

      {step === 1 && (
        <div className="step-intro">
          <h2>Step 1: Create Your Profile</h2>
          <p>Tell us about yourself...</p>
          <button onClick={() => setStep(2)}>Next</button>
        </div>
      )}

      {step === 2 && (
        <div className="step-payment">
          <h2>Step 2: Add a Payment Method</h2>
          <p>Your AI assistant will use this card to make purchases on your behalf.</p>

          <WalletProvider
            publicKey={process.env.REACT_APP_NEKUDA_PUBLIC_KEY}
            userId={user.id}
          >
            <NekudaCollectForm
              visibleSections={[CollectionSection.Payment, CollectionSection.Billing]}
              collectionData={{
                contactInfo: {
                  firstName: user.firstName,
                  lastName: user.lastName,
                  email: user.email
                }
              }}
              onSuccess={(result) => {
                console.log('Card added successfully:', result);
                setStep(3);
              }}
              onError={(error) => {
                console.error('Failed to add card:', error);
              }}
            />
          </WalletProvider>
        </div>
      )}

      {step === 3 && (
        <div className="step-complete">
          <h2>🎉 All Set!</h2>
          <p>Your AI shopping assistant is ready to use.</p>
          <button onClick={() => navigate('/dashboard')}>
            Go to Dashboard
          </button>
        </div>
      )}
    </div>
  );
}
```

**Key Points:**

* Use `NekudaCollectForm` for simple card collection
* Control visible sections with `visibleSections` prop
* Send existing data via `collectionData` prop
* No full wallet UI needed—just add first card
* Redirect to main app after success

See [Collection Form](/frontend/wallet/collect-form) for complete documentation.


---

## [​](#pattern-5:-error-handling-&-recovery) Pattern 5: Error Handling & Recovery

**Use Case:** Handle errors gracefully and guide users to resolution.
**When to Use:**

* Production applications
* Need resilient UX
* Want clear error messages

### [​](#implementation-4) Implementation

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';
import { useState } from 'react';

function RobustWalletIntegration() {
  const { user } = useAuth();
  const [error, setError] = useState(null);
  const [retryCount, setRetryCount] = useState(0);

  const handleError = (error) => {
    console.error('Wallet error:', error);

    // Categorize errors
    if (error.code === 'NETWORK_ERROR') {
      setError({
        type: 'network',
        message: 'Network connection issue. Please check your internet and try again.',
        recoverable: true
      });
    } else if (error.code === 'INVALID_CARD') {
      setError({
        type: 'validation',
        message: 'Invalid card details. Please check and try again.',
        recoverable: true
      });
    } else if (error.code === 'CARD_DECLINED') {
      setError({
        type: 'card',
        message: 'Card was declined. Please use a different card.',
        recoverable: true
      });
    } else {
      setError({
        type: 'unknown',
        message: 'An unexpected error occurred. Our team has been notified.',
        recoverable: false
      });

      // Log to your error tracking service
      logErrorToSentry(error);
    }
  };

  const handleRetry = () => {
    setError(null);
    setRetryCount(prev => prev + 1);
  };

  return (
    <div className="wallet-container">
      {error && (
        <div className={`error-banner error-${error.type}`}>
          <div className="error-content">
            <span className="error-icon">⚠️</span>
            <p>{error.message}</p>
          </div>
          {error.recoverable && (
            <button onClick={handleRetry}>
              Retry
            </button>
          )}
        </div>
      )}

      <WalletProvider
        publicKey={process.env.REACT_APP_NEKUDA_PUBLIC_KEY}
        userId={user.id}
        debug={process.env.NODE_ENV === 'development'}
      >
        <NekudaWallet
          theme="light"
          onError={handleError}
          key={retryCount} // Force remount on retry
        />
      </WalletProvider>
    </div>
  );
}

// Backend error handling
async function handleBackendCardRetrievalErrors(userId, purchaseDetails) {
  const userContext = client.user(String(userId));

  try {
    // Create mandate
    const mandate = new MandateData({ /* ... */ });
    const mandateResponse = await userContext.createMandate(mandate);

    // Request token
    const revealResponse = await userContext.requestCardRevealToken(
      mandateResponse.mandateId
    );

    // Reveal card
    const card = await userContext.revealCardDetails(revealResponse.revealToken);

    return { success: true, card };

  } catch (error) {
    if (error instanceof CardNotFoundError) {
      // User has no saved cards
      return {
        success: false,
        errorCode: 'NO_PAYMENT_METHOD',
        userMessage: 'Please add a payment method in your account settings.',
        needsAction: 'ADD_CARD'
      };
    } else if (error instanceof InvalidRequestError) {
      // Bad request - check mandate data
      console.error('Invalid mandate:', error.message);
      return {
        success: false,
        errorCode: 'INVALID_MANDATE',
        userMessage: 'Unable to process purchase request.',
        needsAction: 'CONTACT_SUPPORT'
      };
    } else if (error instanceof AuthenticationError) {
      // API key issue
      console.error('Auth error:', error.message);
      return {
        success: false,
        errorCode: 'AUTH_ERROR',
        userMessage: 'Service temporarily unavailable.',
        needsAction: 'RETRY_LATER'
      };
    } else if (error instanceof NekudaError) {
      // Other nekuda errors
      console.error('nekuda error:', error.message, error.code);
      return {
        success: false,
        errorCode: error.code || 'NEKUDA_ERROR',
        userMessage: 'Payment processing error. Please try again.',
        needsAction: 'RETRY'
      };
    } else {
      // Unexpected error
      console.error('Unexpected error:', error);
      return {
        success: false,
        errorCode: 'UNKNOWN_ERROR',
        userMessage: 'An unexpected error occurred.',
        needsAction: 'CONTACT_SUPPORT'
      };
    }
  }
}
```

**Key Points:**

* Categorize errors (network, validation, card declined, etc.)
* Show user-friendly error messages
* Provide retry/recovery options
* Log errors to monitoring service
* Handle backend SDK errors with specific error types

---

## [​](#pattern-6:-multi-user/team-accounts-advanced) Pattern 6: Multi-User/Team Accounts (Advanced)

**Advanced Pattern**: This pattern covers complex team/organization scenarios. Most applications can skip this section. Only relevant if you’re building team management features where admins need to view/manage other users’ payment methods.

**Use Case:** Application with multiple users or team members, each with their own payment methods.
**When to Use:**

* Team/organization accounts
* Each user has separate payment methods
* Need to track which user made purchases

### [​](#implementation-5) Implementation

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';

function TeamMemberSettings() {
  const { currentUser, selectedTeamMember } = useTeam();

  // Admin viewing another team member's payment methods
  const isViewingOtherUser = currentUser.id !== selectedTeamMember.id;
  const canEdit = currentUser.role === 'admin' || !isViewingOtherUser;

  return (
    <div className="team-member-settings">
      <header>
        <h2>{selectedTeamMember.name}'s Payment Methods</h2>
        {isViewingOtherUser && (
          <p className="viewing-notice">
            Viewing as admin - purchases will be attributed to {selectedTeamMember.name}
          </p>
        )}
      </header>

      <WalletProvider
        publicKey={process.env.REACT_APP_NEKUDA_PUBLIC_KEY}
        // Use the team member's ID, not the current user's ID
        userId={selectedTeamMember.id}
      >
        <NekudaWallet
          theme="light"
          mode={canEdit ? 'themed' : 'themed'}
          onError={(error) => {
            console.error(`Wallet error for user ${selectedTeamMember.id}:`, error);
          }}
        />
      </WalletProvider>
    </div>
  );
}

// Backend: Track which team member made purchase
app.post('/api/team/purchase', async (req, res) => {
  const currentUser = req.user; // Admin user
  const { teamMemberId, product, price } = req.body;

  // Verify permission
  if (!canUserAccessTeamMember(currentUser, teamMemberId)) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  // Use team member's ID for card retrieval
  const userContext = client.user(String(teamMemberId));

  // ... mandate flow with teamMemberId

  // Record transaction with both IDs
  await db.transactions.create({
    userId: teamMemberId,        // Who the purchase is for
    requestedBy: currentUser.id, // Who initiated it
    product,
    amount: price,
    teamId: currentUser.teamId
  });
});
```

**Key Points:**

* Use correct `userId` for each team member
* Track who initiated purchases vs. whose payment method was used
* Implement proper permission checks
* Show clear UI when viewing other users’ payment methods

---

## [​](#pattern-7:-progressive-enhancement) Pattern 7: Progressive Enhancement

**Use Case:** Start with basic card collection, gradually add features as app matures.
**When to Use:**

* MVP → full product evolution
* Phased feature rollout
* Testing before full deployment

### [​](#evolution-path) Evolution Path

#### [​](#phase-1:-mvp-simple-card-collection) Phase 1: MVP - Simple Card Collection

Copy

Ask AI

```
import { WalletProvider } from '@nekuda/wallet';
import { NekudaCollectForm } from '@nekuda/wallet';

function MVPCardCollection() {
  return (
    <WalletProvider publicKey={publicKey} userId={userId}>
      <NekudaCollectForm
        onSuccess={(result) => {
          alert('Card added! AI agent can now make purchases.');
        }}
      />
    </WalletProvider>
  );
}
```

#### [​](#phase-2:-add-wallet-management) Phase 2: Add Wallet Management

Copy

Ask AI

```
import { WalletProvider, NekudaWallet } from '@nekuda/wallet';

function WalletManagement() {
  return (
    <WalletProvider publicKey={publicKey} userId={userId}>
      {/* Users can now view, add, edit, delete cards */}
      <NekudaWallet theme="light" />
    </WalletProvider>
  );
}
```

#### [​](#phase-3:-add-contact-&-shipping) Phase 3: Add Contact & Shipping

Copy

Ask AI

```
function FullWallet() {
  return (
    <WalletProvider publicKey={publicKey} userId={userId}>
      <NekudaWallet
        theme="light"
        // Now includes Settings tab with contact/shipping
        defaultContact={userContact}
        defaultShipping={userShipping}
        onContactChange={syncContactToYourDB}
        onShippingChange={syncShippingToYourDB}
      />
    </WalletProvider>
  );
}
```

#### [​](#phase-4:-brand-customization) Phase 4: Brand Customization

Copy

Ask AI

```
function BrandedWallet() {
  return (
    <WalletProvider publicKey={publicKey} userId={userId}>
      <NekudaWallet
        mode="custom"
        theme="light"
        styles={{
          // Your brand colors, fonts, spacing
          button: { backgroundColor: brandColors.primary },
          inputFocus: { borderColor: brandColors.primary }
        }}
        defaultContact={userContact}
        defaultShipping={userShipping}
        onContactChange={syncContactToYourDB}
        onShippingChange={syncShippingToYourDB}
      />
    </WalletProvider>
  );
}
```

**Key Points:**

* Start minimal, add features incrementally
* Each phase is production-ready
* No breaking changes between phases
* Test each phase before moving forward

---

## [​](#troubleshooting-guide) Troubleshooting Guide

### [​](#❌-problem-1:-sending-card-data-from-frontend) ❌ Problem 1: Sending Card Data from Frontend

Copy

Ask AI

```
// WRONG - Never send card data from frontend
async function badPurchase(cardData) {
  await fetch('/api/purchase', {
    method: 'POST',
    body: JSON.stringify({
      cardNumber: cardData.cardNumber,  // ❌ NEVER!
      cvv: cardData.cvv                 // ❌ NEVER!
    })
  });
}
```

Copy

Ask AI

```
// CORRECT - Backend retrieves card via nekuda SDK
async function goodPurchase(purchaseDetails) {
  await fetch('/api/purchase', {
    method: 'POST',
    body: JSON.stringify({
      product: purchaseDetails.product,
      price: purchaseDetails.price
      // Backend uses userId from session + nekuda SDK to get card
    })
  });
}
```

### [​](#❌-problem-2:-wrong-userid) ❌ Problem 2: Wrong userId

Copy

Ask AI

```
// WRONG - Using nekuda's internal IDs
<WalletProvider userId={card.id} /> // ❌ card.id is nekuda's ID

// CORRECT - Use YOUR user ID
<WalletProvider userId={yourUser.id} /> // ✅ Your user ID
```

### [​](#❌-problem-3:-not-checking-for-saved-cards) ❌ Problem 3: Not Checking for Saved Cards

Copy

Ask AI

```
// WRONG - Assume user has cards
function badFlow() {
  return <button onClick={makePurchase}>Buy Now</button>;
}

// CORRECT - Check first, prompt if missing
function goodFlow() {
  const wallet = useWallet();

  if (wallet.payments.list.length === 0) {
    return <div>Please add a payment method first.</div>;
  }

  return <button onClick={makePurchase}>Buy Now</button>;
}
```

### [​](#❌-problem-4:-ignoring-default-card-logic) ❌ Problem 4: Ignoring Default Card Logic

Copy

Ask AI

```
// WRONG - Assuming first card is default
const cardToUse = wallet.payments.list[0]; // ❌ Might not be default

// CORRECT - Use the actual default card
const cardToUse = wallet.payments.list.find(c => c.isDefault); // ✅
```

---

## [​](#what’s-next) What’s Next?

[## Wallet Overview

Back to wallet setup and core concepts](/frontend/wallet/overview)[## Styling & Theming

Customize wallet appearance to match your brand](/frontend/wallet/styling-theming)[## Backend SDK Docs

Complete backend SDK documentation](/nekuda-sdk/getting-started)[## Error Handling

Handle errors gracefully in production](/nekuda-sdk/Errors)

---

## [​](#frequently-asked-questions) Frequently Asked Questions

Can I use the wallet without the backend SDK?

No. The wallet is designed for the AI agent use case where your backend retrieves card details via the nekuda backend SDK. The frontend wallet only collects and manages payment method metadata—it never exposes raw card data.

How does the AI agent get the card details?

Your backend uses the nekuda SDK’s 3-step mandate flow:

1. Create mandate (intent to purchase)
2. Request reveal token
3. Reveal card details

Then your AI agent uses those details to fill merchant checkout forms.

What if my user has multiple cards?

The backend SDK retrieves the **default** payment method (the card marked as default, or the most recently added card if no default is set). Users can change their default card in the wallet UI.

Can I customize which card the AI agent uses?

Currently, the backend SDK retrieves the default card. If you need more control, you can:

* Let users set their default card in the wallet
* Build custom UI to let users choose which card for specific purchases
* Use `useWallet().payments.list` to show card options

How do I handle users who haven't added a payment method?

Always check `wallet.payments.list.length > 0` before allowing purchases. If zero, show the wallet UI to prompt card addition. The backend SDK will throw `CardNotFoundError` if you try to retrieve a card for a user with none saved.

What data does the frontend have access to?

The frontend can access non-sensitive metadata via `useWallet().payments.list`:

* Last 4 digits
* Expiry date (MM/YY)
* Card brand (Visa, Mastercard, etc.)
* Cardholder name
* Billing address
* Default status

It **never** has access to full card number or CVV.

How do I test integration patterns in development?

1. Use test mode public key (`pk_test_...`)
2. Add test cards in your dev environment
3. Use test mode secret key (`sk_test_...`) in backend
4. Test the full mandate flow with test data
5. Check nekuda dashboard for test transactions

[Styling & Theming](/frontend/wallet/styling-theming)[Migration Guide](/frontend/wallet/migration-guide)

⌘I

[x](https://x.com/nekuda_ai)[github](https://github.com/nekuda-ai)[linkedin](https://linkedin.com/company/nekuda)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=nekuda)