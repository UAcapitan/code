<?php

namespace App\Controller;

use App\Entity\Bonuses;
use App\Entity\Campaigns;
use App\Entity\Image;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Tags;
use App\Form\BonusesType;
use App\Form\CommentsType;
use App\Form\ImageType;
use App\Form\TagsType;
use Symfony\Component\HttpFoundation\Request;
use App\Entity\Comments;
use App\Entity\Ratings;
use App\Form\RatingsType;
use App\Form\RedactCampaignType;
use App\Entity\News;
use App\Form\NewsType;

class CampaignController extends AbstractController
{
    /**
     * @Route("/campaign/{id}", name="campaign")
     */
    public function index(int $id, Request $request): Response
    {

        $campaign = $this->getDoctrine()->getRepository(Campaigns::class)->find($id);

        $user = $campaign->getUser();

        $tags = new Tags();
        $form = $this->createForm(TagsType::class, $tags);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {

            $tags->setCampaigns($campaign);

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($tags);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $tags_campaign = $this->getDoctrine()->getRepository(Tags::class)->findBy(['campaigns' => $campaign->getId()]);

        $image = new Image();
        $form_image = $this->createForm(ImageType::class, $image);
        $form_image->handleRequest($request);

        if ($form_image->isSubmitted() && $form_image->isValid()) {

            $image->setCampaigns($campaign);

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($image);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $image_campaign = $this->getDoctrine()->getRepository(Image::class)->findBy(['campaigns' => $campaign->getId()]);

        $bonus = new Bonuses();
        $form_bonuses = $this->createForm(BonusesType::class, $bonus);
        $form_bonuses->handleRequest($request);

        if ($form_bonuses->isSubmitted() && $form_bonuses->isValid()) {

            $bonus->setCampaign($campaign);

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($bonus);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $bonuses_campaign = $this->getDoctrine()->getRepository(Bonuses::class)->findBy(['campaign' => $campaign->getId()]);

        if ($campaign->getUser() == $this->getUser()) {
            $check_user = true;
        } else {
            $check_user = false;
        }

        $comments = new Comments();
        $form_comments = $this->createForm(CommentsType::class, $comments);
        $form_comments->handleRequest($request);

        if ($form_comments->isSubmitted() && $form_comments->isValid()) {

            $comments->setCampaign($campaign);
            $comments->setUser($this->getUser());

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($comments);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $comment_campaign = $this->getDoctrine()->getRepository(Comments::class)->findBy(['campaign' => $campaign->getId()], ['id' => 'DESC']);

        $rating = new Ratings();
        $form_rating = $this->createForm(RatingsType::class, $rating);
        $form_rating->handleRequest($request);

        if ($form_rating->isSubmitted() && $form_rating->isValid()) {

            $rating->setCampaigns($campaign);
            $rating->setUser($this->getUser());

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($rating);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $ratings_user = $this->getDoctrine()->getRepository(Ratings::class)->findBy(['campaigns' => $campaign, 'user' => $this->getUser()], ['id' => 'DESC']);

        $ratings = $this->getDoctrine()->getRepository(Ratings::class)->findBy(['campaigns' => $campaign], ['id' => 'DESC']);

        $abs_ratings = 0;
        if (count($ratings) > 0) {
            foreach ($ratings as $r) {
                $abs_ratings += $r->getMark();
            }
            $abs_ratings /= count($ratings);
        }

        $form_redact_campaign = $this->createForm(RedactCampaignType::class, $campaign);
        $form_redact_campaign->handleRequest($request);

        if ($form_redact_campaign->isSubmitted() && $form_redact_campaign->isValid()) {

            $campaign->setUser($campaign->getUser());

            $campaign->setNowMoney($campaign->getNowMoney());

            $campaign->setDate($campaign->getDate());

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($campaign);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $news = new News();
        $form_news = $this->createForm(NewsType::class, $news);
        $form_news->handleRequest($request);

        if ($form_news->isSubmitted() && $form_news->isValid()) {

            $news->setCampaigns($campaign);

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($news);
            $entityManager->flush();

            return $this->redirectToRoute('campaign', ['id' => $campaign->getId()]);
        }

        $news_campaign = $this->getDoctrine()->getRepository(News::class)->findBy(['campaigns' => $campaign->getId()], ['id' => 'DESC'], 5);

        return $this->render('campaign/index.html.twig', [
            'campaign' => $campaign,
            'user' => $user,
            'form' => $form->createView(),
            'tags' => $tags_campaign,
            'form_image' => $form_image->createView(),
            'images' => $image_campaign,
            'form_bonuses' => $form_bonuses->createView(),
            'bonuses' => $bonuses_campaign,
            'check_user' => $check_user,
            'form_comments' => $form_comments->createView(),
            'comments' => $comment_campaign,
            'form_rating' => $form_rating->createView(),
            'rating' => $abs_ratings,
            'ratings' => $ratings_user,
            'form_redact' => $form_redact_campaign->createView(),
            'form_news' => $form_news->createView(),
            'news' => $news_campaign,
        ]);
    }

    /**
     * @Route("/campaign/{id}/delete_tags", name="campaign_delete_tags")
     */
    public function delete_tags(int $id): Response
    {

        $tags_campaign = $this->getDoctrine()->getRepository(Tags::class)->findBy(['campaigns' => $id]);

        $entityManager = $this->getDoctrine()->getManager();
        foreach ($tags_campaign as $tag) {
            $entityManager->remove($tag);
        }
        $entityManager->flush();

        return $this->redirectToRoute('campaign', ['id' => $id]);
    }

    /**
     * @Route("/campaign/{id}/delete", name="campaign_delete")
     */
    public function delete_campaign(int $id): Response
    {

        $campaign = $this->getDoctrine()->getRepository(Campaigns::class)->find($id);

        $entityManager = $this->getDoctrine()->getManager();
        $entityManager->remove($campaign);
        $entityManager->flush();

        return $this->redirectToRoute('profile');
    }
}
