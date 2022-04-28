<?php

namespace App\Controller;

use App\Entity\Campaigns;
use App\Form\CreateCampaignsType;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\HttpFoundation\Request;
use App\Entity\User;

class CreateCampaignsController extends AbstractController
{
    /**
     * @Route("/create_campaign", name="create_campaign")
     */
    public function index(Request $request): Response
    {
        $campaign = new Campaigns();
        $form = $this->createForm(CreateCampaignsType::class, $campaign);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {

            $campaign->setUser($this->getUser());

            $campaign->setNowMoney(0);

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($campaign);
            $entityManager->flush();

            return $this->redirectToRoute('index_page');
        }

        return $this->render('create_campaigns/index.html.twig', [
            'form' => $form->createView(),
        ]);
    }

    /**
     * @Route("/create_campaign/{id}", name="create_campaign_admin")
     */
    public function create_campaign_admin(Request $request, int $id): Response
    {
        $campaign = new Campaigns();
        $form = $this->createForm(CreateCampaignsType::class, $campaign);
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {

            $campaign->setUser($user);

            $campaign->setNowMoney(0);

            $entityManager = $this->getDoctrine()->getManager();
            $entityManager->persist($campaign);
            $entityManager->flush();

            return $this->redirectToRoute('index_page');
        }

        return $this->render('create_campaigns/index.html.twig', [
            'form' => $form->createView(),
        ]);
    }
}
